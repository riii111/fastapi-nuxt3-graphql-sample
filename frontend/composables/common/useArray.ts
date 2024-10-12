export const filterValid = <T> (array: readonly T[] | null | undefined) => (
  array?.filter(item => !!item) ?? []
) as readonly (T & {})[]
