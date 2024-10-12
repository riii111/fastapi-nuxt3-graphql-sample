/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type UserCreateByAdmin = {
    email: string;
    password?: string;
    organization_id_list?: Array<string>;
    is_notification_on?: boolean;
    notification_days_before_list?: Array<number>;
    name?: string;
    first_name?: string;
    last_name?: string;
    forced_password_change?: boolean;
    permission_id?: string;
    team_id_list?: Array<string>;
};

