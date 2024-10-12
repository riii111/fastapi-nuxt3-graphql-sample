import { UnauthorizeError } from '~/class/errors/UnauthorizeError'
import type { HttpMethod } from '~/enums/HttpMethod'

// GET以外はnever
type FetchParams<T, M extends HttpMethod> = M extends 'GET' ? T : never
// GETだったらnever
type FetchBody<T, M extends HttpMethod> = M extends 'POST' | 'PUT' | 'DELETE' ? T : never
// GETだったらどっちも可能、それ以外だったらLazyのみ
type IsLazy<M extends HttpMethod> = M extends 'GET' ? boolean : false

interface IFetchOptions <T extends Record<string, any>, M extends HttpMethod> {
  headers?: Record<string, any>
  method: M
  params?: FetchParams<T, M>
  body?: FetchBody<T, M>
  cache?: RequestCache | undefined
  isLazy: IsLazy<M>
}

export function useCoreApi () {
  const config = useRuntimeConfig()
  const {
    getCookie,
    COOKIE_KEY
  } = useCookies()

  const metaInfo = computed(() => ({
    apiServerBase: config.public.apiServerBase,
    apiServerBaseV1: `${config.public.apiServerBase}/api/v1`,
    apiClientBase: config.public.apiClientBase,
    apiClientBaseV1: `${config.public.apiClientBase}/api/v1`
  }))

  function genAuthHeader () {
    return {
      Authorization: `Bearer ${getCookie(COOKIE_KEY.accessToken).value}`
    }
  }

  async function customFetch <
    M extends HttpMethod,
    RequestInput extends Record<string, any> = Record<string, any>,
    RequestResult = unknown,
  > (
    url: string,
    {
      headers: optionHeaders,
      method,
      body: optionBody,
      params,
      cache = 'no-cache',
      isLazy
    }: IFetchOptions<RequestInput, M>
  ) {
    const authHeader = genAuthHeader()
    const headers = {
      ...optionHeaders,
      ...authHeader
    }

    const fetch = isLazy
      ? useLazyFetch<RequestResult>
      : useFetch<RequestResult>

    const body = (() => {
      if (!optionBody) {
        return undefined
      }

      const urlParams = new URLSearchParams()
      Object.keys(optionBody).forEach((key) => {
        urlParams.append(key, optionBody[key])
      })
      return urlParams
    })()

    const response = await fetch(url, {
      headers,
      // useFetchはGETしか対応していないのでエラーが出ているが、GET以外の時はisLazyがfalseにしか設定できないよう型で縛っているので問題なしとする
      // @ts-expect-error
      method,
      body,
      params,
      cache
      // TODO: requestErrorやresponseError処理等実装する
    })

    if (!response.error.value) {
      return response
    }

    // エラー処理
    if (response.error.value.statusCode === 401) {
      throw new UnauthorizeError()
    }

    throw response.error.value
  }

  return {
    config,
    COOKIE_KEY,
    customFetch,
    metaInfo
  }
}
