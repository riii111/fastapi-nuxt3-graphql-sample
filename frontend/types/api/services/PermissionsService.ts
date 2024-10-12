/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { OrganizationUserPermissionsPublic } from '../models/OrganizationUserPermissionsPublic';
import type { PermissionPublic } from '../models/PermissionPublic';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class PermissionsService {

    /**
     * Get All Permissions
     * @returns PermissionPublic Successful Response
     * @throws ApiError
     */
    public static getAllPermissionsApiV1PermissionsGet(): CancelablePromise<Array<PermissionPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/permissions/',
        });
    }

    /**
     * Update Organization User Permission
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static updateOrganizationUserPermissionApiV1PermissionsPut(
        requestBody: OrganizationUserPermissionsPublic,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/permissions/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
