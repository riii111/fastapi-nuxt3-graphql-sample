import type { ValidationRule } from '~/types/vuetify/Form'
type ValidationType = 'required' | `max-${number}` | `min-${number}` | 'email' | 'tel' | 'numeric' | 'url' | 'zip' | 'kana'

export const useValidation = () => {
  return {
    buildValidationRules,
    zip,
    email,
    tel,
    max,
    min,
    numeric,
    required,
    kana
  }
}

const buildValidationRules = (types: ValidationType[], customValidation?: ValidationRule []) => {
  const rules = filterValid(
    types.map((type) => {
      if (type === 'required') {
        return required
      }

      if (type.includes('max')) {
        const num = Number(type.split('-')[1])
        if (Number.isNaN(num)) {
          throw new TypeError('不正な値です。')
        }

        return max(num)
      }

      if (type.includes('min')) {
        const num = Number(type.split('-')[1])
        if (Number.isNaN(num)) {
          throw new TypeError('不正な値です。')
        }

        return min(num)
      }

      if (type === 'kana') {
        return kana
      }

      if (type === 'email') {
        return email
      }

      if (type === 'tel') {
        return tel
      }

      if (type === 'numeric') {
        return numeric
      }

      if (type === 'url') {
        return url
      }

      if (type === 'zip') {
        return zip
      }

      return undefined
    })
  ) as ValidationRule[]

  return [
    ...rules,
    ...customValidation ?? []
  ]
}

const zip = (zipCode: string) => {
  // ハイフンなしのパターンとハイフンありのパターンを正規表現でチェック
  const pattern = /^\d{7}$|^\d{3}-\d{4}$/
  return pattern.test(zipCode) || '無効な郵便番号です'
}

const url = (val: string): string | boolean => {
  if (!val) {
    // 未入力の場合はチェックしない
    return true
  }
  const re = /^http(|s):\/\/.+/

  return re.test(val) || '無効なURLです'
}

const email = (val: string): string | boolean => {
  if (!val) {
    // 未入力の場合はチェックしない
    return true
  }
  const pattern = /^(([^\s"(),.:;<>@[\\\]]+(\.[^\s"(),.:;<>@[\\\]]+)*)|(".+"))@((\[(?:\d{1,3}\.){3}\d{1,3}])|(([\dA-Za-z]+\.)+[A-Za-z]{2,}))$/

  return pattern.test(val) || 'メールアドレスの形式で入力してください'
}

const kana = (val: string) => {
  const pattern = /^[\u30A1-\u30FF]+$/

  return pattern.test(val) || 'カタカナで入力してください'
}

const tel = (val: string): string | boolean => {
  if (!val) {
    // 未入力の場合はチェックしない
    return true
  }

  const pattern = /^\d{10,11}$/
  return pattern.test(val) || '電話番号の形式が間違っています'
}

const numeric = (val: string): string | boolean => {
  if (!val) {
    // 未入力の場合はチェックしない
    return true
  }

  // 純粋な数字の文字列
  const isNumeric = !Number.isNaN(Number(val.toString().trim()))

  return isNumeric || '数値で入力してください'
}

const max = (length = 300): boolean | ValidationRule => {
  if (length <= 0) {
    return true
  }

  return (val: string) => {
    if (!val) {
      // 未入力の場合はチェックしない
      return true
    }

    const msg = `${length}文字以下で入力してください`
    return val.length <= length || msg
  }
}

const min = (length: number): boolean | ValidationRule => {
  if (length <= 0) {
    return true
  }

  return (val: string) => {
    if (!val) {
      // 未入力の場合はチェックしない
      return true
    }
    const msg = `${length}文字以上で入力してください`
    return val.length >= length || msg
  }
}

const required = (val: string | number | File | undefined | null | any[]): string | boolean => {
  const message = '入力必須項目です'
  // autocompleteコンポーネント複数選択用の入力チェック
  if (Array.isArray(val)) {
    return val.length > 0 || message
  }

  // v-file-inputコンポーネント用の入力チェック
  if (val instanceof File) {
    return !!val.name || message
  }

  return (val !== null && val !== undefined && val !== '') || message
}

export const nonNull = <T>(val: T) => {
  if (val === undefined || val === null) {
    throw new TypeError('必要な情報がありません')
  }
  return val
}
