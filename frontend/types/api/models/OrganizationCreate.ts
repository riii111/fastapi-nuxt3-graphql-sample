/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type OrganizationCreate = {
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
};

