from http import HTTPStatus
from random import randint
from unittest import mock
from urllib.error import HTTPError
from uuid import uuid4

import pandas as pd
import pytest
from django.conf import settings

from rest_framework.test import APITestCase


class TestDisplayView(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.doc_id = str(uuid4())
        self.sheet_id = randint(0, 10**10)
        self.sheet_data = pd.DataFrame({"something": ["a", "b"]})
        self.base_endpoint_url = f"/display/doc/{self.doc_id}/"
        self.base_fetch_url = (
            f"{settings.GOOGLE_URL}/{self.doc_id}/export?format="
            f"{settings.EXPORT_FORMAT}"
        )

    def test_success_no_sheet_id(self):
        client = self.client_class()

        with mock.patch.object(
            pd,
            "read_csv",
            return_value=self.sheet_data,
        ) as mocker:
            response = client.get(self.base_endpoint_url)

        assert response.status_code == HTTPStatus.OK
        mocker.assert_called_with(self.base_fetch_url)  # No sheet_id

    def test_success_with_sheet_id(self):
        client = self.client_class()

        with mock.patch.object(
            pd,
            "read_csv",
            return_value=self.sheet_data,
        ) as mocker:
            response = client.get(f"{self.base_endpoint_url}sheet/{self.sheet_id}/")

        assert response.status_code == HTTPStatus.OK
        mocker.assert_called_with(f"{self.base_fetch_url}&gid={self.sheet_id}")

    def test_failed_data_fetch(self):
        client = self.client_class()
        with mock.patch.object(
            pd,
            "read_csv",
            side_effect=HTTPError(
                url=self.base_endpoint_url,
                code=0,
                msg="",
                hdrs=None,
                fp=None,
            ),
        ) as mocker:
            with pytest.raises(Exception) as error:
                client.get(self.base_endpoint_url)

        assert mocker.call_count == 1
        assert str(error.value) == "Failed to fetch sheet data."
