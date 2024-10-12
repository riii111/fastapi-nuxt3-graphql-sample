/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type TodoPublic = {
    /**
     * ToDo名
     */
    name?: string;
    /**
     * プリセットフラグ
     */
    is_preset?: boolean;
    /**
     * ToDo番号
     */
    number: number;
    /**
     * ステータス
     */
    status?: number;
    /**
     * 担当者
     */
    assignee_user_id?: string;
    /**
     * 開始日
     */
    start_at?: string;
    /**
     * 終了日
     */
    end_at: string;
    /**
     * カテゴリID
     */
    category_id_list: Array<string>;
    /**
     * 備考
     */
    notice?: string;
    /**
     * 組織ID
     */
    orgnization_id: string;
    /**
     * イベントID
     */
    event_id: string;
    /**
     * タスクID
     */
    task_id: string;
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

