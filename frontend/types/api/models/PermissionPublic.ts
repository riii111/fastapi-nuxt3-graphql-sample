/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { PermissionsEnum } from './PermissionsEnum';

export type PermissionPublic = {
    name: string;
    internal_name: PermissionsEnum;
    /**
     * イベントカテゴリーの閲覧作成編集可能有無 -1:権限なし 0:閲覧可 1:閲覧編集可 2:閲覧編集作成削除可
     */
    manage_category: number;
    /**
     * ユーザーの閲覧作成編集可能有無
     */
    manage_user: number;
    /**
     * チームの閲覧作成編集可能有無
     */
    manage_user_group: number;
    /**
     * チームの閲覧作成編集可能有無
     */
    manage_quotation: number;
    /**
     * 関連会社の閲覧作成編集可能有無
     */
    manage_service_plan: number;
    /**
     * 相識の閲覧作成編集可能有無
     */
    manage_organization_group: number;
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

