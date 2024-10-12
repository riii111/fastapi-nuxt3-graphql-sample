/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TeamCreate } from '../models/TeamCreate';
import type { TeamPublic } from '../models/TeamPublic';
import type { TeamsDelete } from '../models/TeamsDelete';
import type { TeamUpdatable } from '../models/TeamUpdatable';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TeamsService {

    /**
     * Get All Teams
     * @param organizationId
     * @returns TeamPublic Successful Response
     * @throws ApiError
     */
    public static getAllTeamsApiV1TeamsGet(
        organizationId: string,
    ): CancelablePromise<Array<TeamPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/teams/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Insert One
     * @param organizationId
     * @param requestBody
     * @returns TeamPublic Successful Response
     * @throws ApiError
     */
    public static insertOneApiV1TeamsPost(
        organizationId: string,
        requestBody: TeamCreate,
    ): CancelablePromise<TeamPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/teams/',
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
     * Delete Many
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteManyApiV1TeamsDelete(
        requestBody: TeamsDelete,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/teams/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update One
     * @param teamId
     * @param requestBody
     * @returns TeamPublic Successful Response
     * @throws ApiError
     */
    public static updateOneApiV1TeamsTeamIdPut(
        teamId: string,
        requestBody: TeamUpdatable,
    ): CancelablePromise<TeamPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/teams/{team_id}/',
            path: {
                'team_id': teamId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
