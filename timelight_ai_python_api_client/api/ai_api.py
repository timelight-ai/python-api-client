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


class AIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_ai_anomalies_source_id_get(self, source_id, **kwargs):  # noqa: E501
        """Auto detect-anomalies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_anomalies_source_id_get(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float source_id: (required)
        :return: AnomaliesResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ai_anomalies_source_id_get_with_http_info(source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_ai_anomalies_source_id_get_with_http_info(source_id, **kwargs)  # noqa: E501
            return data

    def v1_ai_anomalies_source_id_get_with_http_info(self, source_id, **kwargs):  # noqa: E501
        """Auto detect-anomalies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_anomalies_source_id_get_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float source_id: (required)
        :return: AnomaliesResponseDto
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
                    " to method v1_ai_anomalies_source_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_ai_anomalies_source_id_get`")  # noqa: E501

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
            '/v1/ai/anomalies/{sourceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnomaliesResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_ai_recompute_day_models_source_id_year_post(self, year, source_id, **kwargs):  # noqa: E501
        """Recomputes all day modesl  # noqa: E501

        Erases and re-computes all day models for a source and year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_day_models_source_id_year_post(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: RecomputeDayModelsResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ai_recompute_day_models_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_ai_recompute_day_models_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
            return data

    def v1_ai_recompute_day_models_source_id_year_post_with_http_info(self, year, source_id, **kwargs):  # noqa: E501
        """Recomputes all day modesl  # noqa: E501

        Erases and re-computes all day models for a source and year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_day_models_source_id_year_post_with_http_info(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: RecomputeDayModelsResponseDto
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
                    " to method v1_ai_recompute_day_models_source_id_year_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `v1_ai_recompute_day_models_source_id_year_post`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_ai_recompute_day_models_source_id_year_post`")  # noqa: E501

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
            '/v1/ai/recompute-day-models/{sourceId}/{year}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecomputeDayModelsResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_ai_recompute_days_projection_source_id_year_post(self, year, source_id, **kwargs):  # noqa: E501
        """Computes all days projection for a source and save them  # noqa: E501

        This computes the X/Y projection of all days in the source for the given year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_days_projection_source_id_year_post(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: RecomputeDaysProjectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ai_recompute_days_projection_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_ai_recompute_days_projection_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
            return data

    def v1_ai_recompute_days_projection_source_id_year_post_with_http_info(self, year, source_id, **kwargs):  # noqa: E501
        """Computes all days projection for a source and save them  # noqa: E501

        This computes the X/Y projection of all days in the source for the given year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_days_projection_source_id_year_post_with_http_info(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :return: RecomputeDaysProjectionResponseDto
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
                    " to method v1_ai_recompute_days_projection_source_id_year_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `v1_ai_recompute_days_projection_source_id_year_post`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_ai_recompute_days_projection_source_id_year_post`")  # noqa: E501

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
            '/v1/ai/recompute-days-projection/{sourceId}/{year}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecomputeDaysProjectionResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_ai_recompute_models_source_id_year_post(self, year, source_id, **kwargs):  # noqa: E501
        """Triggers a model recompute  # noqa: E501

        This operations erases both non-handled alerts and user previsions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_models_source_id_year_post(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :param float model_count:
        :return: RecomputeModelsResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ai_recompute_models_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_ai_recompute_models_source_id_year_post_with_http_info(year, source_id, **kwargs)  # noqa: E501
            return data

    def v1_ai_recompute_models_source_id_year_post_with_http_info(self, year, source_id, **kwargs):  # noqa: E501
        """Triggers a model recompute  # noqa: E501

        This operations erases both non-handled alerts and user previsions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_models_source_id_year_post_with_http_info(year, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float year: (required)
        :param float source_id: (required)
        :param float model_count:
        :return: RecomputeModelsResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'source_id', 'model_count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_ai_recompute_models_source_id_year_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `v1_ai_recompute_models_source_id_year_post`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_ai_recompute_models_source_id_year_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'year' in params:
            path_params['year'] = params['year']  # noqa: E501
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']  # noqa: E501

        query_params = []
        if 'model_count' in params:
            query_params.append(('modelCount', params['model_count']))  # noqa: E501

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
            '/v1/ai/recompute-models/{sourceId}/{year}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecomputeModelsResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_ai_recompute_source_models_model_count_post(self, model_count, **kwargs):  # noqa: E501
        """Triggers a model recompute for source groups  # noqa: E501

        This operations erases the group configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_source_models_model_count_post(model_count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float model_count: (required)
        :return: RecomputeSourceModelsResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ai_recompute_source_models_model_count_post_with_http_info(model_count, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_ai_recompute_source_models_model_count_post_with_http_info(model_count, **kwargs)  # noqa: E501
            return data

    def v1_ai_recompute_source_models_model_count_post_with_http_info(self, model_count, **kwargs):  # noqa: E501
        """Triggers a model recompute for source groups  # noqa: E501

        This operations erases the group configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ai_recompute_source_models_model_count_post_with_http_info(model_count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float model_count: (required)
        :return: RecomputeSourceModelsResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_ai_recompute_source_models_model_count_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_count' is set
        if ('model_count' not in params or
                params['model_count'] is None):
            raise ValueError("Missing the required parameter `model_count` when calling `v1_ai_recompute_source_models_model_count_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_count' in params:
            path_params['modelCount'] = params['model_count']  # noqa: E501

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
            '/v1/ai/recompute-source-models/{modelCount}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecomputeSourceModelsResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
