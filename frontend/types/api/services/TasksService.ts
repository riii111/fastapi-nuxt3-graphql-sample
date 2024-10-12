/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TaskCreate } from '../models/TaskCreate';
import type { TaskPublic } from '../models/TaskPublic';
import type { TaskUpdate } from '../models/TaskUpdate';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TasksService {

    /**
     * Get Tasks
     * タスク情報を全件取得します
     * @param organizationId
     * @returns TaskPublic タスク情報一覧
     * @throws ApiError
     */
    public static getTasksApiV1TasksGet(
        organizationId: string,
    ): CancelablePromise<Array<TaskPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/tasks/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Registry Task
     * タスク情報を登録します
     * @param organizationId
     * @param requestBody
     * @returns TaskPublic 登録したタスク情報
     * @throws ApiError
     */
    public static registryTaskApiV1TasksPost(
        organizationId: string,
        requestBody: TaskCreate,
    ): CancelablePromise<TaskPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/tasks/',
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
     * Get Task
     * 指定IDのタスク情報を取得します
     * @param taskId
     * @param organizationId
     * @returns TaskPublic タスク情報
     * @throws ApiError
     */
    public static getTaskApiV1TasksTaskIdGet(
        taskId: string,
        organizationId: string,
    ): CancelablePromise<TaskPublic> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/tasks/{task_id}/',
            path: {
                'task_id': taskId,
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
     * Update Task
     * 指定IDのタスク情報を更新します
     * @param taskId
     * @param requestBody
     * @returns TaskPublic 更新後タスク情報
     * @throws ApiError
     */
    public static updateTaskApiV1TasksTaskIdPut(
        taskId: string,
        requestBody: TaskUpdate,
    ): CancelablePromise<TaskPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/tasks/{task_id}/',
            path: {
                'task_id': taskId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Task
     * 指定IDのタスク情報を削除します
     * @param taskId
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteTaskApiV1TasksTaskIdDelete(
        taskId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/tasks/{task_id}/',
            path: {
                'task_id': taskId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
