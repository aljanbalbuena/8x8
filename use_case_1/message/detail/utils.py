from requests import Response, HTTPError


def try_raise_status(response: Response) -> None:
    try:
        response.raise_for_status()
    except HTTPError as error:
        # Can further expand to use custom exceptions if needed
        if 400 <= response.status_code < 500:
            raise Exception("Client side error.") from error

        raise error
