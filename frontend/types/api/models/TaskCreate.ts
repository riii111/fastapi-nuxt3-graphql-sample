/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type TaskCreate = {
    /**
     * タスク名
     */
    name?: string;
    /**
     * 責任者
     */
    person_in_charge?: string;
    /**
     * 開始日
     */
    start_at?: string;
    /**
     * 終了日
     */
    end_at: string;
    /**
     * 備考
     */
    note?: string;
    /**
     * 親イベントID
     */
    parent_event_id?: string;
    /**
     * 組織ID
     */
    orgnization_id: string;
};

