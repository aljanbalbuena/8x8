from pandas import DataFrame


class DataProcessor:
    @staticmethod
    def merge(
        data_a: DataFrame, data_b: DataFrame, column: str, how: str = "outer"
    ) -> DataFrame:
        """
        More on dataframe merging at pandas documentation
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

        :param data_a:
            Dataframe to merge to (will appear on left)
        :param data_b:
            Dataframe to merge (will appear on right)
        :param column:
            Common column on where to merge at
        :param how:
            1. outer = keep all rows
            2. inner = discard rows with no shared common column value
        :return:
        """
        return data_a.merge(data_b, left_on=column, right_on=column, how=how)
