/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Avatar } from './Avatar';

export type UserPublic = {
    access_token?: string;
    refresh_token?: string;
    token_type?: string;
    email?: string;
    first_name?: string;
    last_name?: string;
    furigana?: string;
    nickname?: string;
    avator?: Avatar;
    forced_password_change?: boolean;
    is_notification_on?: boolean;
    notification_days_before_list?: Array<number>;
    login_failure_count?: number;
    is_logged_in?: boolean;
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

