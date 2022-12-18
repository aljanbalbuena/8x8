# Use Case 3

Merge two csv files on a common column

## Prerequisites

- Python 3+

## How to run

1. Install required libraries listed in `requirements.txt`
2. Replace text values in `script.py` as needed.
    ```python
    """
    Init(
        "Input file path",
        "Input file path",
        "Column where to merge two input",
        "Output file path",
    )
    """
    processor = Init("CSV1.csv", "CSV2.csv", "name", "CSV3.csv")
    ```
3. Run `script.py`

## Tests

1. Change directory to test folder `cd tests`
2. Run `python -m pytest`
