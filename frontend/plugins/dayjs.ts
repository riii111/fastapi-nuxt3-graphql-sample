import { locale, extend } from 'dayjs'
import weekday from 'dayjs/plugin/weekday'
import relativeTime from 'dayjs/plugin/relativeTime'
import 'dayjs/locale/ja'

export default defineNuxtPlugin(() => {
  extend(weekday)
  extend(relativeTime)
  locale('ja')
})
