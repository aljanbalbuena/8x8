from http import HTTPStatus
from random import randint

import pytest
import requests_mock

from django.conf import settings

from rest_framework.test import APITestCase


class TestRetrieveParameters(APITestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.intl_number = randint(10**9, 10**10) + 10**10
        self.country_code = "US"
        self.messagebird_response = {
            "href": f"https://rest.messagebird.com/lookup/{self.intl_number}",
            "countryCode": self.country_code,
            "countryPrefix": 1,
            "phoneNumber": self.intl_number,
            "type": "fixed line or mobile",
            "formats": {
                "e164": f"+{self.intl_number}",
                "international": "+1 408-555-1212",
                "national": "(408) 555-1212",
                "rfc3966": "tel:+1-408-555-1212",
            },
        }

    def test_success(self):
        client = self.client_class()

        with requests_mock.Mocker() as mock:
            mock.get(
                f"{settings.MESSAGEBIRD_URL}/{self.intl_number}",
                json=self.messagebird_response,
                status_code=HTTPStatus.OK,
            )

            response = client.post("/detail/", {"ANI": self.intl_number}, format="json")

        assert response.status_code == HTTPStatus.OK
        assert response.data == {
            "countryCode": self.country_code,
            "countryPrefix": 1,
            "e164": f"+{self.intl_number}",
        }

    def test_client_error(self):  # This app as MessageBirdAPI client
        client = self.client_class()

        with requests_mock.Mocker() as mock:
            for status in [HTTPStatus.BAD_REQUEST, HTTPStatus.UNAUTHORIZED]:
                mock.get(
                    f"{settings.MESSAGEBIRD_URL}/{self.intl_number}",
                    status_code=status,
                )

                with pytest.raises(Exception) as error:
                    client.post("/detail/", {"ANI": self.intl_number}, format="json")

                assert str(error.value) == "Client side error."

    def test_missing_field(self):
        client = self.client_class()
        with pytest.raises(KeyError):
            client.post("/detail/", {"some_key": self.intl_number}, format="json")
