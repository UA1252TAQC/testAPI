from http import HTTPStatus

import logging as log

import allure
import pytest

from api.base_api import BaseApi
from modules.constants import Data


@pytest.mark.comment
@allure.feature('Delete Comment Feature')
@allure.story('Mark comment in Eco News as deleted')
@allure.severity(allure.severity_level.NORMAL)
def test_delete_comment_success(tc_logger,
                                get_auth_token,
                                setup_comment):
    try:
        test_name = "Verify successful deletion of a comment from news."
        tc_logger.log_test_name(test_name)
        log.info(f"Test '{test_name}' started")

        comment_id = setup_comment.json()['id']

        api = BaseApi(f'{Data.API_BASE_URL}/econews/comments?id={comment_id}')
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {get_auth_token}'
        }
        response = api.delete_data(headers=headers)
        log.info(f"Response status code: {response.status_code}")

        assert response.status_code == HTTPStatus.OK
        log.info(f"Comment with ID: {comment_id} deleted")
        log.info(f"Test {test_name} completed.")

    except Exception as e:
        log.error(f"An error occurred: {str(e)}")
        pytest.fail(f"Test failed due to an unexpected error: {str(e)}")
