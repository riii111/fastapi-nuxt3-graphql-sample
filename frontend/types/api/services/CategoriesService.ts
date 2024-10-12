/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CategoriesDelete } from '../models/CategoriesDelete';
import type { CategoryCreate } from '../models/CategoryCreate';
import type { CategoryPublic } from '../models/CategoryPublic';
import type { CategoryUpdatable } from '../models/CategoryUpdatable';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class CategoriesService {

    /**
     * Get All Categories
     * カテゴリ一覧を取得する
     * @param organizationId
     * @returns CategoryPublic カテゴリ一覧
     * @throws ApiError
     */
    public static getAllCategoriesApiV1CategoriesGet(
        organizationId: string,
    ): CancelablePromise<Array<CategoryPublic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/categories/',
            query: {
                'organization_id': organizationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Registry Category
     * 新規でカテゴリを登録する
     * @param organizationId
     * @param requestBody
     * @returns CategoryPublic 登録したカテゴリの情報
     * @throws ApiError
     */
    public static registryCategoryApiV1CategoriesPost(
        organizationId: string,
        requestBody: CategoryCreate,
    ): CancelablePromise<CategoryPublic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/categories/',
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
     * Delete Categories
     * 指定のカテゴリを削除する
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteCategoriesApiV1CategoriesDelete(
        requestBody: CategoriesDelete,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/categories/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Category
     * 指定IDのカテゴリを更新する
     * @param categoryId
     * @param requestBody
     * @returns CategoryPublic 更新したカテゴリの情報
     * @throws ApiError
     */
    public static updateCategoryApiV1CategoriesCategoryIdPut(
        categoryId: string,
        requestBody: CategoryUpdatable,
    ): CancelablePromise<CategoryPublic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/categories/{category_id}/',
            path: {
                'category_id': categoryId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
