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


class PrevisionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_prevision_group_apply_prevision_post(self, prevision_apply_group_dto, **kwargs):  # noqa: E501
        """Apply a source prevision to the whole group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_group_apply_prevision_post(prevision_apply_group_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrevisionApplyGroupDto prevision_apply_group_dto: (required)
        :return: PrevisionApplyGroupResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_prevision_group_apply_prevision_post_with_http_info(prevision_apply_group_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_prevision_group_apply_prevision_post_with_http_info(prevision_apply_group_dto, **kwargs)  # noqa: E501
            return data

    def v1_prevision_group_apply_prevision_post_with_http_info(self, prevision_apply_group_dto, **kwargs):  # noqa: E501
        """Apply a source prevision to the whole group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_group_apply_prevision_post_with_http_info(prevision_apply_group_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrevisionApplyGroupDto prevision_apply_group_dto: (required)
        :return: PrevisionApplyGroupResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prevision_apply_group_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_prevision_group_apply_prevision_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prevision_apply_group_dto' is set
        if ('prevision_apply_group_dto' not in params or
                params['prevision_apply_group_dto'] is None):
            raise ValueError("Missing the required parameter `prevision_apply_group_dto` when calling `v1_prevision_group_apply_prevision_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'prevision_apply_group_dto' in params:
            body_params = params['prevision_apply_group_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/prevision/group-apply-prevision', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrevisionApplyGroupResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_prevision_list_source_id_year_get(self, year, source_id, **kwargs):  # noqa: E501
        """Fetch data previsions for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_list_source_id_year_get(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: PrevisionListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_prevision_list_source_id_year_get_with_http_info(year, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_prevision_list_source_id_year_get_with_http_info(year, source_id, **kwargs)  # noqa: E501
            return data

    def v1_prevision_list_source_id_year_get_with_http_info(self, year, source_id, **kwargs):  # noqa: E501
        """Fetch data previsions for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_list_source_id_year_get_with_http_info(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: PrevisionListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'source_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_prevision_list_source_id_year_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `v1_prevision_list_source_id_year_get`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_prevision_list_source_id_year_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'year' in params:
            path_params['year'] = params['year']  # noqa: E501
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
            '/v1/prevision/list/{sourceId}/{year}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrevisionListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_prevision_save_default_previsions_source_id_year_post(self, year, source_id, **kwargs):  # noqa: E501
        """Generate default previsions for the source and save them  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_save_default_previsions_source_id_year_post(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: PrevisionBulkSaveResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_prevision_save_default_previsions_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_prevision_save_default_previsions_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
            return data

    def v1_prevision_save_default_previsions_source_id_year_post_with_http_info(self, year, source_id, **kwargs):  # noqa: E501
        """Generate default previsions for the source and save them  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_save_default_previsions_source_id_year_post_with_http_info(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: PrevisionBulkSaveResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'source_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_prevision_save_default_previsions_source_id_year_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `v1_prevision_save_default_previsions_source_id_year_post`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_prevision_save_default_previsions_source_id_year_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'year' in params:
            path_params['year'] = params['year']  # noqa: E501
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
            '/v1/prevision/save-default-previsions/{sourceId}/{year}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrevisionBulkSaveResultDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_prevision_save_post(self, prevision_bulk_save_dto, **kwargs):  # noqa: E501
        """Save many previsions at once  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_save_post(prevision_bulk_save_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrevisionBulkSaveDto prevision_bulk_save_dto: (required)
        :return: PrevisionBulkSaveResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_prevision_save_post_with_http_info(prevision_bulk_save_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_prevision_save_post_with_http_info(prevision_bulk_save_dto, **kwargs)  # noqa: E501
            return data

    def v1_prevision_save_post_with_http_info(self, prevision_bulk_save_dto, **kwargs):  # noqa: E501
        """Save many previsions at once  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_save_post_with_http_info(prevision_bulk_save_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrevisionBulkSaveDto prevision_bulk_save_dto: (required)
        :return: PrevisionBulkSaveResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prevision_bulk_save_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_prevision_save_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prevision_bulk_save_dto' is set
        if ('prevision_bulk_save_dto' not in params or
                params['prevision_bulk_save_dto'] is None):
            raise ValueError("Missing the required parameter `prevision_bulk_save_dto` when calling `v1_prevision_save_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'prevision_bulk_save_dto' in params:
            body_params = params['prevision_bulk_save_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/prevision/save', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrevisionBulkSaveResultDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_prevision_update_patch(self, prevision_patch_dto, **kwargs):  # noqa: E501
        """Update a specific prevision  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_update_patch(prevision_patch_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrevisionPatchDto prevision_patch_dto: (required)
        :return: PrevisionUpdateResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_prevision_update_patch_with_http_info(prevision_patch_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_prevision_update_patch_with_http_info(prevision_patch_dto, **kwargs)  # noqa: E501
            return data

    def v1_prevision_update_patch_with_http_info(self, prevision_patch_dto, **kwargs):  # noqa: E501
        """Update a specific prevision  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_prevision_update_patch_with_http_info(prevision_patch_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrevisionPatchDto prevision_patch_dto: (required)
        :return: PrevisionUpdateResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prevision_patch_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_prevision_update_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prevision_patch_dto' is set
        if ('prevision_patch_dto' not in params or
                params['prevision_patch_dto'] is None):
            raise ValueError("Missing the required parameter `prevision_patch_dto` when calling `v1_prevision_update_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'prevision_patch_dto' in params:
            body_params = params['prevision_patch_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/prevision/update', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrevisionUpdateResultDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
