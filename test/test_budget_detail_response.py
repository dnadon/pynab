# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pynab
from pynab.models.budget_detail_response import BudgetDetailResponse  # noqa: E501
from pynab.rest import ApiException


class TestBudgetDetailResponse(unittest.TestCase):
    """BudgetDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBudgetDetailResponse(self):
        """Test BudgetDetailResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = pynab.models.budget_detail_response.BudgetDetailResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
