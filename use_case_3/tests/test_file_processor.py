import itertools

import pytest as pytest

from processor import FileProcessor


@pytest.fixture
def fp():
    return FileProcessor()


def test_success(fp):
    """
    Expected content from fixture: (tab delimited)
    COL_0	    COL_1
    row_0_col_0	row_0_col_1
    row_1_col_0	row_1_col_1
    """
    dataframe = fp.read_csv("fixtures/read_test.csv")

    assert set(dataframe.columns) == {"COL_0", "COL_1"}
    for a, b in itertools.product([0, 1], [0, 1]):
        assert dataframe.loc[a][b] == f"row_{a}_col_{b}"


def test_not_csv(fp):
    with pytest.raises(Exception) as error:
        fp.read_csv("fixtures/some_file.extension")

    assert str(error.value) == "File type not supported"


def test_not_found(fp):
    file_path = "fixtures/non_existing_file.csv"
    with pytest.raises(FileNotFoundError) as error:
        fp.read_csv(file_path)

    assert f"No such file or directory: '{file_path}'" in str(error.value)
