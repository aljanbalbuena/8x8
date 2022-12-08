# Use Case 1

Retrieve details from MessageBird

## Prerequisites

- Python 3.9

## How to run

1. Install required libraries listed in `requirements.txt`
2. Create server
    ```
    cd message
    python manage.py runserver
    ```

4. Access endpoint
    * URL: `http://localhost:8000/detail/`
    * Method: `POST`
    * Headers: `None`
    * Payload:
        ```json
        {
          "ANI": "14085551212"
        }
        ```

## Tests

1. If using a virtual environment make sure to activate it first `source venv/bin/activate`
2. Run `python manage.py test`
