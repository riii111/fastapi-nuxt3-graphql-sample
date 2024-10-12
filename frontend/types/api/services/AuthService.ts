/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_login_api_v1_auth_login__post } from '../models/Body_login_api_v1_auth_login__post';
import type { Message } from '../models/Message';
import type { RequestResetPassword } from '../models/RequestResetPassword';
import type { ResetPassword } from '../models/ResetPassword';
import type { UserPublic } from '../models/UserPublic';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AuthService {

    /**
     * Login
     * @param formData
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static loginApiV1AuthLoginPost(
        formData: Body_login_api_v1_auth_login__post,
    ): CancelablePromise<UserPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/auth/login/',
            formData: formData,
            mediaType: 'application/x-www-form-urlencoded',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Token Refresh
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static tokenRefreshApiV1AuthTokenRefreshPost(): CancelablePromise<UserPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/auth/token/refresh/',
        });
    }

    /**
     * Request Reset Password Send Email
     * @param requestBody
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static requestResetPasswordSendEmailApiV1AuthResetPasswordSendEmailPost(
        requestBody: RequestResetPassword,
    ): CancelablePromise<Message> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/auth/reset/password/send/email/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Request Reset Password
     * @param requestBody
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static requestResetPasswordApiV1AuthResetPasswordPost(
        requestBody: ResetPassword,
    ): CancelablePromise<Message> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/auth/reset/password/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
