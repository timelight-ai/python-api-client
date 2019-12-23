# coding: utf-8

"""
    timelight

    This is the timelight api.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from timelight_ai_python_api_client.api_client import ApiClient


class ModelApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_model_bulk_patch(self, models_patch_dto, **kwargs):  # noqa: E501
        """Model bulk update  # noqa: E501

        Update many models at once, mainly used to set color and name of the model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_bulk_patch(models_patch_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsPatchDto models_patch_dto: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_model_bulk_patch_with_http_info(models_patch_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_model_bulk_patch_with_http_info(models_patch_dto, **kwargs)  # noqa: E501
            return data

    def v1_model_bulk_patch_with_http_info(self, models_patch_dto, **kwargs):  # noqa: E501
        """Model bulk update  # noqa: E501

        Update many models at once, mainly used to set color and name of the model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_bulk_patch_with_http_info(models_patch_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsPatchDto models_patch_dto: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['models_patch_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_model_bulk_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'models_patch_dto' is set
        if ('models_patch_dto' not in params or
                params['models_patch_dto'] is None):
            raise ValueError("Missing the required parameter `models_patch_dto` when calling `v1_model_bulk_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'models_patch_dto' in params:
            body_params = params['models_patch_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/model/bulk', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_model_bulk_replace_source_id_post(self, models_post_dto, source_id, **kwargs):  # noqa: E501
        """Custom Model create  # noqa: E501

        Create many custom models at once, this config replaces the original models.        WARNING: This action will remove all previsions and alerts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_bulk_replace_source_id_post(models_post_dto, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsPostDto models_post_dto: (required)
        :param float source_id: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_model_bulk_replace_source_id_post_with_http_info(models_post_dto, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_model_bulk_replace_source_id_post_with_http_info(models_post_dto, source_id, **kwargs)  # noqa: E501
            return data

    def v1_model_bulk_replace_source_id_post_with_http_info(self, models_post_dto, source_id, **kwargs):  # noqa: E501
        """Custom Model create  # noqa: E501

        Create many custom models at once, this config replaces the original models.        WARNING: This action will remove all previsions and alerts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_bulk_replace_source_id_post_with_http_info(models_post_dto, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsPostDto models_post_dto: (required)
        :param float source_id: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['models_post_dto', 'source_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_model_bulk_replace_source_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'models_post_dto' is set
        if ('models_post_dto' not in params or
                params['models_post_dto'] is None):
            raise ValueError("Missing the required parameter `models_post_dto` when calling `v1_model_bulk_replace_source_id_post`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_model_bulk_replace_source_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'models_post_dto' in params:
            body_params = params['models_post_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/model/bulk-replace/{sourceId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_model_list_get(self, **kwargs):  # noqa: E501
        """List models data of this source  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_model_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_model_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_model_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """List models data of this source  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_model_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/model/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_model_list_source_id_get(self, source_id, **kwargs):  # noqa: E501
        """List models data of this source  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_list_source_id_get(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float source_id: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_model_list_source_id_get_with_http_info(source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_model_list_source_id_get_with_http_info(source_id, **kwargs)  # noqa: E501
            return data

    def v1_model_list_source_id_get_with_http_info(self, source_id, **kwargs):  # noqa: E501
        """List models data of this source  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_list_source_id_get_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float source_id: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_model_list_source_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_model_list_source_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/model/list/{sourceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_model_reset_source_id_model_count_post(self, model_count, source_id, **kwargs):  # noqa: E501
        """Reset to default timelight models configuration  # noqa: E501

        Drop all models and re-create them from data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_reset_source_id_model_count_post(model_count, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float model_count: (required)
        :param float source_id: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_model_reset_source_id_model_count_post_with_http_info(model_count, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_model_reset_source_id_model_count_post_with_http_info(model_count, source_id, **kwargs)  # noqa: E501
            return data

    def v1_model_reset_source_id_model_count_post_with_http_info(self, model_count, source_id, **kwargs):  # noqa: E501
        """Reset to default timelight models configuration  # noqa: E501

        Drop all models and re-create them from data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_model_reset_source_id_model_count_post_with_http_info(model_count, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float model_count: (required)
        :param float source_id: (required)
        :return: ModelListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_count', 'source_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_model_reset_source_id_model_count_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_count' is set
        if ('model_count' not in params or
                params['model_count'] is None):
            raise ValueError("Missing the required parameter `model_count` when calling `v1_model_reset_source_id_model_count_post`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_model_reset_source_id_model_count_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_count' in params:
            path_params['modelCount'] = params['model_count']  # noqa: E501
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/model/reset/{sourceId}/{modelCount}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
