
import allure
import pytest
import logging
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants


class TestCreateBooking():
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        LOGGER=logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase-TC1")
        response=post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )

        verify_http_status_code(response_data=response,expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        print(response.bookingid)
        LOGGER.info(response.json()["bookingid"])
        LOGGER.info("End of the Testcase TC1 -positive")

    @pytest.mark.negative
    @allure.title("Verify that Create Booking doesn't work with no payload")
    @allure.description(
        "Creating a Booking with no payload and verify that booking id")
    def test_create_booking_negative(self):
        response=post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response,expected_data=500)