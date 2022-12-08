import json
from http import HTTPStatus

import requests

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .utils import try_raise_status


@api_view(("POST",))
@renderer_classes((JSONRenderer,))
def retrieve_parameters(request: WSGIRequest) -> Response:
    """
    Retrieve details from MessageBirdAPI
    """
    number = json.loads(request.body)["ANI"]

    response = requests.get(
        f"{settings.MESSAGEBIRD_URL}/{number}",
        headers={"Authorization": f"AccessKey {settings.TEST_KEY}"},
    )
    try_raise_status(response)
    body = response.json()

    return Response(
        {
            "countryCode": body["countryCode"],
            "countryPrefix": body["countryPrefix"],
            "e164": body["formats"]["e164"],
        },
        status=HTTPStatus.OK,
    )
