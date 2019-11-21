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

from timelight-ai-python-api-client.api_client import ApiClient


class ImportApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_import_create_source_post(self, create_source_dto, **kwargs):  # noqa: E501
        """First source creation  # noqa: E501

        Creates a source, add a first batch of day data, then computes the models for the first time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_create_source_post(create_source_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateSourceDto create_source_dto: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v1_import_create_source_post_with_http_info(create_source_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_import_create_source_post_with_http_info(create_source_dto, **kwargs)  # noqa: E501
            return data

    def v1_import_create_source_post_with_http_info(self, create_source_dto, **kwargs):  # noqa: E501
        """First source creation  # noqa: E501

        Creates a source, add a first batch of day data, then computes the models for the first time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_create_source_post_with_http_info(create_source_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateSourceDto create_source_dto: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_source_dto']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_import_create_source_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_source_dto' is set
        if ('create_source_dto' not in params or
                params['create_source_dto'] is None):
            raise ValueError("Missing the required parameter `create_source_dto` when calling `v1_import_create_source_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_source_dto' in params:
            body_params = params['create_source_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/import/create-source', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_import_days_post(self, import_days_dto, **kwargs):  # noqa: E501
        """Add new data to a source  # noqa: E501

        When new data is added, we compute alerts for this data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_days_post(import_days_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param ImportDaysDto import_days_dto: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v1_import_days_post_with_http_info(import_days_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_import_days_post_with_http_info(import_days_dto, **kwargs)  # noqa: E501
            return data

    def v1_import_days_post_with_http_info(self, import_days_dto, **kwargs):  # noqa: E501
        """Add new data to a source  # noqa: E501

        When new data is added, we compute alerts for this data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_days_post_with_http_info(import_days_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param ImportDaysDto import_days_dto: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['import_days_dto']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_import_days_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'import_days_dto' is set
        if ('import_days_dto' not in params or
                params['import_days_dto'] is None):
            raise ValueError("Missing the required parameter `import_days_dto` when calling `v1_import_days_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'import_days_dto' in params:
            body_params = params['import_days_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/import/days', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_import_reprocess_days_source_id_year_post(self, year, source_id, **kwargs):  # noqa: E501
        """Reprocess days from database  # noqa: E501

        Compute maps, alerts and closest models  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_reprocess_days_source_id_year_post(year, source_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param float year: (required)
        :param float source_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v1_import_reprocess_days_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_import_reprocess_days_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
            return data

    def v1_import_reprocess_days_source_id_year_post_with_http_info(self, year, source_id, **kwargs):  # noqa: E501
        """Reprocess days from database  # noqa: E501

        Compute maps, alerts and closest models  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_reprocess_days_source_id_year_post_with_http_info(year, source_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param float year: (required)
        :param float source_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'source_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_import_reprocess_days_source_id_year_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `v1_import_reprocess_days_source_id_year_post`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_import_reprocess_days_source_id_year_post`")  # noqa: E501

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
            '/v1/import/reprocess-days/{sourceId}/{year}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_import_source_id_days_post(self, source_id, import_days_dto, **kwargs):  # noqa: E501
        """Add new data to a source  # noqa: E501

        When new data is added, we compute alerts for this data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_source_id_days_post(source_id, import_days_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param float source_id: (required)
        :param ImportDaysDto import_days_dto: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v1_import_source_id_days_post_with_http_info(source_id, import_days_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_import_source_id_days_post_with_http_info(source_id, import_days_dto, **kwargs)  # noqa: E501
            return data

    def v1_import_source_id_days_post_with_http_info(self, source_id, import_days_dto, **kwargs):  # noqa: E501
        """Add new data to a source  # noqa: E501

        When new data is added, we compute alerts for this data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v1_import_source_id_days_post_with_http_info(source_id, import_days_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param float source_id: (required)
        :param ImportDaysDto import_days_dto: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id', 'import_days_dto']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_import_source_id_days_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_import_source_id_days_post`")  # noqa: E501
        # verify the required parameter 'import_days_dto' is set
        if ('import_days_dto' not in params or
                params['import_days_dto'] is None):
            raise ValueError("Missing the required parameter `import_days_dto` when calling `v1_import_source_id_days_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'import_days_dto' in params:
            body_params = params['import_days_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/import/{sourceId}/days', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
