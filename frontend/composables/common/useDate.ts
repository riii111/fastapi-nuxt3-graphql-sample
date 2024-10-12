import dayjs from 'dayjs'
import 'dayjs/plugin/weekday'

export function useDate () {
  return {
    isWeekDay,
    isFirstWeekdayOfMonth
  }
}

function isWeekDay (input: string | Date | dayjs.Dayjs) {
  const date = dayjs(input)
  const dayOfWeek = date.weekday()
  // 0は日曜日、6は土曜日
  if (dayOfWeek < 1 || dayOfWeek > 5) {
    return false
  }
  return true
}

function isFirstWeekdayOfMonth (input: string | Date) {
  const date = dayjs(input)
  // 月初3日以内に必ず月初の平日は存在する
  if (date.date() > 3 || !isWeekDay(date)) {
    return false
  }

  // 月初から3日を調査する
  const firstDayOfMonth = dayjs(date).startOf('month')
  for (let i = 0; i < 3; i++) {
    const checkingDay = firstDayOfMonth.add(i, 'day')
    // 月で一番最初の平日が、propsで渡されたdateと一致していたらtrueを返す
    if (isWeekDay(checkingDay)) {
      return checkingDay.isSame(date, 'day')
    }
  }

  return false
}
