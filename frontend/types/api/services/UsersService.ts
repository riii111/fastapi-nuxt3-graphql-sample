/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_import_users_api_v1_users_import__post } from '../models/Body_import_users_api_v1_users_import__post';
import type { UserCreate } from '../models/UserCreate';
import type { UserCreateByAdmin } from '../models/UserCreateByAdmin';
import type { UserDetailedPublic } from '../models/UserDetailedPublic';
import type { UserPasswordUpdateInEndpoint } from '../models/UserPasswordUpdateInEndpoint';
import type { UserPublic } from '../models/UserPublic';
import type { UsersBase } from '../models/UsersBase';
import type { UsersTeamsUpdate } from '../models/UsersTeamsUpdate';
import type { UserUpdatable } from '../models/UserUpdatable';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class UsersService {

    /**
     * Get User List
     * @param organizationId
     * @returns UserDetailedPublic Successful Response
     * @throws ApiError
     */
    public static getUserListApiV1UsersGet(
        organizationId: string,
    ): CancelablePromise<Array<UserDetailedPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Many
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteManyApiV1UsersDelete(
        requestBody: UsersBase,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/users/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Insert One
     * @param requestBody
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static insertOneApiV1UsersSignupPost(
        requestBody: UserCreate,
    ): CancelablePromise<UserPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/users/signup/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Insert One As Admin
     * @param organizationId
     * @param requestBody
     * @returns UserCreate Successful Response
     * @throws ApiError
     */
    public static insertOneAsAdminApiV1UsersCreatePost(
        organizationId: string,
        requestBody: UserCreateByAdmin,
    ): CancelablePromise<UserCreate> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/users/create/',
            query: {
                'organization_id': organizationId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Find Me
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static findMeApiV1UsersMeGet(): CancelablePromise<UserPublic> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/me/',
        });
    }

    /**
     * Update Me
     * @param requestBody
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static updateMeApiV1UsersMePut(
        requestBody: UserUpdatable,
    ): CancelablePromise<UserPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/users/me/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Users Teams
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static updateUsersTeamsApiV1UsersTeamsPut(
        requestBody: UsersTeamsUpdate,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/users/teams/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * User Self Password Change
     * @param requestBody
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static userSelfPasswordChangeApiV1UsersMePasswordPut(
        requestBody: UserPasswordUpdateInEndpoint,
    ): CancelablePromise<UserPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/users/me/password/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Current User Logout
     * @returns any Successful Response
     * @throws ApiError
     */
    public static currentUserLogoutApiV1UsersMeLogoutPost(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/users/me/logout/',
        });
    }

    /**
     * Find Colleagues
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static findColleaguesApiV1UsersMeColleaguesGet(): CancelablePromise<Array<UserPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/me/colleagues/',
        });
    }

    /**
     * Import Users
     * @param organizationId
     * @param formData
     * @returns UserCreate Successful Response
     * @throws ApiError
     */
    public static importUsersApiV1UsersImportPost(
        organizationId: string,
        formData: Body_import_users_api_v1_users_import__post,
    ): CancelablePromise<Array<UserCreate>> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/users/import/',
            query: {
                'organization_id': organizationId,
            },
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Export Users
     * @param organizationId
     * @returns any Successful Response
     * @throws ApiError
     */
    public static exportUsersApiV1UsersExportGet(
        organizationId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/export/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
