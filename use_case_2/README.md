# Use Case 1

Retrieve details from MessageBird

## Prerequisites

- Python 3.9

## How to run

1. Install required libraries listed in `requirements.txt`
2. Create server 
   ```
   cd spreadsheet
   python manage.py runserver
   ```

3. Access endpoint <br>
    * URL: `http://localhost:8000/display/doc/{document_id}/`  
    * Method: `GET`
    * Headers: `None`
    * Payload: `None`

    The `document_id` can be found in the Google Docs URL. 
    ```json
    # Sample URL
    "https://docs.google.com/spreadsheets/d/1m3vhA2A2ACOfcKJnfjGPybyIlQwYPxIyMf0F0gJjgHQ"
    The value after "/d/"  is the "document_id": "1m3vhA2A2ACOfcKJnfjGPybyIlQwYPxIyMf0F0gJjgHQ"
    ``` 


## Tests

1. If using a virtual environment make sure to activate it first `source venv/bin/activate`
2. Run `python manage.py test`
