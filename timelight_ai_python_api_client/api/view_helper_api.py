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


class ViewHelperApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_view_helper_alerts_get(self, **kwargs):  # noqa: E501
        """Get the alert view data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_view_helper_alerts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_view_helper_alerts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_view_helper_alerts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_view_helper_alerts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the alert view data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_view_helper_alerts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method v1_view_helper_alerts_get" % key
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
            '/v1/view-helper/alerts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_view_helper_alerts_ref_get(self, **kwargs):  # noqa: E501
        """Get the alert referential view data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_view_helper_alerts_ref_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AlertRefResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_view_helper_alerts_ref_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_view_helper_alerts_ref_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_view_helper_alerts_ref_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the alert referential view data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_view_helper_alerts_ref_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AlertRefResultDto
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
                    " to method v1_view_helper_alerts_ref_get" % key
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
            '/v1/view-helper/alerts-ref', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlertRefResultDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_view_helper_days_near_date_source_id_day_date_get(self, day_date, source_id, **kwargs):  # noqa: E501
        """Get the alert modal view data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_view_helper_days_near_date_source_id_day_date_get(day_date, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str day_date: (required)
        :param float source_id: (required)
        :return: DaysNearDateResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_view_helper_days_near_date_source_id_day_date_get_with_http_info(day_date, source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_view_helper_days_near_date_source_id_day_date_get_with_http_info(day_date, source_id, **kwargs)  # noqa: E501
            return data

    def v1_view_helper_days_near_date_source_id_day_date_get_with_http_info(self, day_date, source_id, **kwargs):  # noqa: E501
        """Get the alert modal view data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_view_helper_days_near_date_source_id_day_date_get_with_http_info(day_date, source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str day_date: (required)
        :param float source_id: (required)
        :return: DaysNearDateResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['day_date', 'source_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_view_helper_days_near_date_source_id_day_date_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'day_date' is set
        if ('day_date' not in params or
                params['day_date'] is None):
            raise ValueError("Missing the required parameter `day_date` when calling `v1_view_helper_days_near_date_source_id_day_date_get`")  # noqa: E501
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `v1_view_helper_days_near_date_source_id_day_date_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'day_date' in params:
            path_params['dayDate'] = params['day_date']  # noqa: E501
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
            '/v1/view-helper/days-near-date/{sourceId}/{dayDate}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DaysNearDateResultDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
