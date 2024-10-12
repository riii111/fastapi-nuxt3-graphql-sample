// Cookieのキー、定数として持つ
const COOKIE_KEY = {
  accessToken: 'accessToken',
  refreshToken: 'refreshToken'
}

export function useCookies () {
  function setCookie (key: string, value: string | null, options?: any) {
    const cookie = useCookie(key, options)
    cookie.value = value
  }

  function getCookie (key: string) {
    const cookie = useCookie(key)
    return cookie
  }

  return {
    COOKIE_KEY,
    setCookie,
    getCookie
  }
}
