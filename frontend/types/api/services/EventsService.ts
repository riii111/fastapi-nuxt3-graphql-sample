/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { EventCreate } from '../models/EventCreate';
import type { EventPublic } from '../models/EventPublic';
import type { EventUpdatable } from '../models/EventUpdatable';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class EventsService {

    /**
     * Get All Events
     * イベントの一覧を取得する
     * @param organizationId
     * @returns EventPublic イベント一覧
     * @throws ApiError
     */
    public static getAllEventsApiV1EventsGet(
        organizationId: string,
    ): CancelablePromise<Array<EventPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/events/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Post Event
     * 新規でイベントを登録する
     * @param organizationId
     * @param requestBody
     * @returns EventPublic 登録したイベントの情報
     * @throws ApiError
     */
    public static postEventApiV1EventsPost(
        organizationId: string,
        requestBody: EventCreate,
    ): CancelablePromise<EventPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/events/',
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
     * Get Event
     * 指定IDのイベントを取得する
     * @param eventId
     * @param organizationId
     * @returns EventPublic 取得したイベントの情報
     * @throws ApiError
     */
    public static getEventApiV1EventsEventIdGet(
        eventId: string,
        organizationId: string,
    ): CancelablePromise<EventPublic> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/events/{event_id}/',
            path: {
                'event_id': eventId,
            },
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Event
     * 指定IDのイベント情報を更新する
     * @param eventId
     * @param requestBody
     * @returns EventPublic 更新したイベントの情報
     * @throws ApiError
     */
    public static updateEventApiV1EventsEventIdPut(
        eventId: string,
        requestBody: EventUpdatable,
    ): CancelablePromise<EventPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/events/{event_id}/',
            path: {
                'event_id': eventId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Event
     * 指定IDのイベント情報を削除する
     * @param eventId
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteEventApiV1EventsEventIdDelete(
        eventId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/events{event_id}/',
            path: {
                'event_id': eventId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
