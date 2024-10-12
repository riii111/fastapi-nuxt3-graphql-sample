/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TodoCreate } from '../models/TodoCreate';
import type { TodoPublic } from '../models/TodoPublic';
import type { TodoUpdate } from '../models/TodoUpdate';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TodosService {

    /**
     * Get All Todos
     * ToDoを一覧を取得する
     * @param organizationId
     * @returns TodoPublic ToDo一覧
     * @throws ApiError
     */
    public static getAllTodosApiV1TodosGet(
        organizationId: string,
    ): CancelablePromise<Array<TodoPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/todos/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Registry Todo
     * 新規でToDoを登録する
     * @param organizationId
     * @param requestBody
     * @returns TodoPublic 登録したToDoの情報
     * @throws ApiError
     */
    public static registryTodoApiV1TodosPost(
        organizationId: string,
        requestBody: TodoCreate,
    ): CancelablePromise<TodoPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/todos/',
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
     * Get Todo
     * 指定IDのToDoを取得する
     * @param todoId
     * @param organizationId
     * @returns TodoPublic 取得したToDoの情報
     * @throws ApiError
     */
    public static getTodoApiV1TodosTodoIdGet(
        todoId: string,
        organizationId: string,
    ): CancelablePromise<TodoPublic> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/todos/{todo_id}/',
            path: {
                'todo_id': todoId,
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
     * Update Todo
     * 指定IDのToDo情報を更新する
     * @param todoId
     * @param requestBody
     * @returns TodoPublic 更新したToDoの情報
     * @throws ApiError
     */
    public static updateTodoApiV1TodosTodoIdPut(
        todoId: string,
        requestBody: TodoUpdate,
    ): CancelablePromise<TodoPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/todos{todo_id}/',
            path: {
                'todo_id': todoId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Todo
     * 指定IDのToDo情報を削除する
     * @param todoId
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteTodoApiV1TodosTodoIdDelete(
        todoId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/todos{todo_id}/',
            path: {
                'todo_id': todoId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
