# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pynab.api_client import ApiClient


class BudgetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_budget_by_id(self, budget_id, **kwargs):  # noqa: E501
        """Single budget  # noqa: E501

        Returns a single budget with all related entities.  This resource is effectively a full budget export.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budget_by_id(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :param int last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
        :return: BudgetDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_budget_by_id_with_http_info(budget_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_budget_by_id_with_http_info(budget_id, **kwargs)  # noqa: E501
            return data

    def get_budget_by_id_with_http_info(self, budget_id, **kwargs):  # noqa: E501
        """Single budget  # noqa: E501

        Returns a single budget with all related entities.  This resource is effectively a full budget export.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budget_by_id_with_http_info(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :param int last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
        :return: BudgetDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id', 'last_knowledge_of_server']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_budget_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if ('budget_id' not in params or
                params['budget_id'] is None):
            raise ValueError("Missing the required parameter `budget_id` when calling `get_budget_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501

        query_params = []
        if 'last_knowledge_of_server' in params:
            query_params.append(('last_knowledge_of_server', params['last_knowledge_of_server']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BudgetDetailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_budget_settings_by_id(self, budget_id, **kwargs):  # noqa: E501
        """Budget Settings  # noqa: E501

        Returns settings for a budget  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budget_settings_by_id(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :return: BudgetSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_budget_settings_by_id_with_http_info(budget_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_budget_settings_by_id_with_http_info(budget_id, **kwargs)  # noqa: E501
            return data

    def get_budget_settings_by_id_with_http_info(self, budget_id, **kwargs):  # noqa: E501
        """Budget Settings  # noqa: E501

        Returns settings for a budget  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budget_settings_by_id_with_http_info(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :return: BudgetSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_budget_settings_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if ('budget_id' not in params or
                params['budget_id'] is None):
            raise ValueError("Missing the required parameter `budget_id` when calling `get_budget_settings_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BudgetSettingsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_budgets(self, **kwargs):  # noqa: E501
        """List budgets  # noqa: E501

        Returns budgets list with summary information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budgets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_accounts: Whether to include the list of budget accounts
        :return: BudgetSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_budgets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_budgets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_budgets_with_http_info(self, **kwargs):  # noqa: E501
        """List budgets  # noqa: E501

        Returns budgets list with summary information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budgets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_accounts: Whether to include the list of budget accounts
        :return: BudgetSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_accounts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_budgets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_accounts' in params:
            query_params.append(('include_accounts', params['include_accounts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BudgetSummaryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
