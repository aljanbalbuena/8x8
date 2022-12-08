import pandas as pd
import pytest
import numpy as np

from processor import DataProcessor


@pytest.fixture
def dp():
    return DataProcessor()


@pytest.fixture
def order():
    return {"Order": ["First", "Second", "Third", "Fourth"]}


@pytest.fixture
def arabic():
    return {"Arabic": [1, 2, 3, 4]}


@pytest.fixture
def roman():
    return {"Roman": ["I", "II", "III", "IV"]}


@pytest.fixture
def df_a(arabic, order):
    data = {**arabic, **order}
    return pd.DataFrame(data)


@pytest.fixture
def df_b(roman, order):
    data = {**roman, **order}
    return pd.DataFrame(data)


def test_success(
    dp,
    df_a,
    df_b,
    arabic,
    roman,
    order,
):
    merged_data = dp.merge(df_a, df_b, "Order")

    expected_data = pd.DataFrame({**arabic, **order, **roman})

    assert expected_data.to_string() == merged_data.to_string()
    assert len(df_a) == len(df_b) == len(merged_data)


def test_misaligned_common_column(dp, df_a):
    roman_data = {
        "Roman": ["II", "III", "IV", "V"],
        "Order": ["Second", "Third", "Fourth", "Fifth"],
    }
    df_b = pd.DataFrame(roman_data)

    merged_data = dp.merge(df_a, df_b, "Order")

    expected_data = pd.DataFrame(
        {
            "Arabic": [1, 2, 3, 4, np.NAN],
            "Order": ["First", "Second", "Third", "Fourth", "Fifth"],
            "Roman": [np.NAN, "II", "III", "IV", "V"],
        }
    )

    assert expected_data.to_string() == merged_data.to_string()
    assert len(merged_data) > len(df_b)
    assert len(merged_data) > len(df_a)
