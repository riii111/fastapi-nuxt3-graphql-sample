/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { OrganizationCreate } from '../models/OrganizationCreate';
import type { OrganizationPublic } from '../models/OrganizationPublic';
import type { OrganizationUpdatable } from '../models/OrganizationUpdatable';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class OrganizationsService {

    /**
     * Get All Organizations
     * 所属している組織一覧を取得する
     * @returns OrganizationPublic 組織一覧
     * @throws ApiError
     */
    public static getAllOrganizationsApiV1OrganizationsGet(): CancelablePromise<Array<OrganizationPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/organizations/',
        });
    }

    /**
     * Post Organization
     * 新規で組織を登録する
     * @param requestBody
     * @returns OrganizationPublic 登録した組織の情報
     * @throws ApiError
     */
    public static postOrganizationApiV1OrganizationsPost(
        requestBody: OrganizationCreate,
    ): CancelablePromise<OrganizationPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/organizations/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Organization
     * 指定IDの組織を取得する
     * @param organizationId
     * @returns OrganizationPublic 取得した組織の情報
     * @throws ApiError
     */
    public static getOrganizationApiV1OrganizationsOrganizationIdGet(
        organizationId: string,
    ): CancelablePromise<OrganizationPublic> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/organizations/{organization_id}/',
            path: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Organization
     * 指定IDの組織情報を更新する
     * @param organizationId
     * @param requestBody
     * @returns OrganizationPublic 更新した組織の情報
     * @throws ApiError
     */
    public static updateOrganizationApiV1OrganizationsOrganizationIdPut(
        organizationId: string,
        requestBody: OrganizationUpdatable,
    ): CancelablePromise<OrganizationPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/organizations/{organization_id}/',
            path: {
                'organization_id': organizationId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
