/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type OrganizationPublic = {
    /**
     * 組織名
     */
    name?: string;
    /**
     * 組織タイプ
     */
    type: number;
    /**
     * 会社規模
     */
    volume?: string;
    /**
     * 従業員数
     */
    employee_amount?: number;
    /**
     * 上場/非上場
     */
    is_listed?: boolean;
    /**
     * 公開/非公開
     */
    is_public?: boolean;
    /**
     * 本店/支店
     */
    is_head?: boolean;
    /**
     * 決算月
     */
    closing_at?: string;
    /**
     * 監査役 設置/非設置
     */
    is_auditor?: boolean;
    /**
     * 有価証券報告書提出会社 該当/非該当
     */
    is_securities_report?: boolean;
    /**
     * 親組織ID
     */
    parent_organization_id?: Array<string>;
    /**
     * 代表者ID
     */
    delegate_user_id?: string;
    /**
     * 顧客情報ID
     */
    customer_id: string;
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

