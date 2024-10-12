export enum Status {
  TODO = 'TODO',
  IN_PROGRESS = 'IN_PROGRESS',
  RESOLVED = 'RESOLVED',
  COMPLETED = 'COMPLETED'
}

export const StatusJapaneseMap: Record<Status, string> = {
  [Status.TODO]: '未対応',
  [Status.IN_PROGRESS]: '対応中',
  [Status.RESOLVED]: '対応済み',
  [Status.COMPLETED]: '完了'
}
