/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AffiliatedOrganizationCreate } from '../models/AffiliatedOrganizationCreate';
import type { AffiliatedOrganizationPublic } from '../models/AffiliatedOrganizationPublic';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AffiliatedOrganizationsService {

    /**
     * Get Affiliated Organizations
     * @param organizationId
     * @returns AffiliatedOrganizationPublic Successful Response
     * @throws ApiError
     */
    public static getAffiliatedOrganizationsApiV1AffiliatedOrganizationsGet(
        organizationId: string,
    ): CancelablePromise<Array<AffiliatedOrganizationPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/affiliated_organizations/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Create Affiliated Organization
     * @param organizationId
     * @param requestBody
     * @returns AffiliatedOrganizationPublic Successful Response
     * @throws ApiError
     */
    public static createAffiliatedOrganizationApiV1AffiliatedOrganizationsPost(
        organizationId: string,
        requestBody: AffiliatedOrganizationCreate,
    ): CancelablePromise<AffiliatedOrganizationPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/affiliated_organizations/',
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

}
