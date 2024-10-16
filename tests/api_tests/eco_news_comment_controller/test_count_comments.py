from http import HTTPStatus

import logging as log

import allure
import pytest

from api.base_api import BaseApi
from modules.constants import Data


@pytest.mark.comment
@allure.feature('Count Comments Feature')
@allure.story('Count Comments in Eco News')
@allure.severity(allure.severity_level.NORMAL)
def test_count_comments_success(tc_logger,
                                get_auth_token,
                                setup_and_teardown_news,
                                setup_comment):
    try:
        test_name = "Verify successful retrieval of the comment count for the news post."
        tc_logger.log_test_name(test_name)
        log.info(f"Test '{test_name}' started")

        news_id = setup_and_teardown_news

        log.info(f"Starting test {test_name}")
        api = BaseApi(
            f'{Data.API_BASE_URL}/econews/comments/count/comments/{news_id}'
        )
        headers = {
            'accept': '*/*'
        }
        response = api.get_data(headers=headers)
        log.info(f"Response status code: {response.status_code}")

        assert response.status_code == HTTPStatus.OK

        response_data = response.json()
        log.info(f"Retrieved comment count: {response_data}")

        assert response_data == 1
        log.info("Comment count verification successful.")

    except Exception as e:
        log.error(f"An error occurred: {str(e)}")
        pytest.fail(f"Test failed due to an unexpected error: {str(e)}")
