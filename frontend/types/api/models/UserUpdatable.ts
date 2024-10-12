/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Avatar } from './Avatar';

export type UserUpdatable = {
    email?: string;
    first_name?: string;
    last_name?: string;
    furigana?: string;
    nickname?: string;
    avator?: Avatar;
    forced_password_change?: boolean;
    is_notification_on?: boolean;
    notification_days_before_list?: Array<number>;
};

