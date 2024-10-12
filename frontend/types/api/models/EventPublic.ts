/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type EventPublic = {
    /**
     * イベント名
     */
    name?: string;
    /**
     * プリセットフラグ
     */
    is_preset?: boolean;
    /**
     * ステータス
     */
    status?: number;
    /**
     * 責任者
     */
    person_in_charge?: string;
    /**
     * カテゴリID
     */
    category_id_list: Array<string>;
    /**
     * 備考
     */
    note?: string;
    /**
     * イベント説明
     */
    explain?: string;
    /**
     * 関連法令
     */
    related_law?: string;
    /**
     * キータスク
     */
    key_task?: string;
    /**
     * 組織ID
     */
    organization_id: string;
    /**
     * 関連イベントID
     */
    related_event_id_list?: Array<string>;
    /**
     * 閲覧者
     */
    viewer_user_id_list?: Array<string>;
    /**
     * 編集者
     */
    editor_user_id_list?: Array<string>;
    /**
     * オーナー
     */
    owner_user_id?: string;
    /**
     * 閲覧可チーム
     */
    viewer_team_id_list?: Array<string>;
    /**
     * 編集可チーム
     */
    editor_team_id_list?: Array<string>;
    /**
     * 作成日時
     */
    created_at?: string;
    /**
     * 更新日時
     */
    updated_at?: string;
    /**
     * オブジェクトID
     */
    _id: string;
};

