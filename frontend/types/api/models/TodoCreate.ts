/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type TodoCreate = {
    /**
     * ToDo名
     */
    name?: string;
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
     * 備考
     */
    notice?: string;
    /**
     * 組織ID
     */
    organaization_id: string;
};

