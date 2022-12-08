import pandas as pd
from pandas import DataFrame


class FileProcessor:
    def __init__(
        self,
        separator: str = "\t",
    ):
        self.separator = separator

    def read_csv(self, file_path: str) -> DataFrame:
        if file_path.split(".")[-1] != "csv":
            raise Exception("File type not supported")

        return pd.read_csv(file_path, sep=self.separator, dtype=str)

    def write_csv(self, dataframe: DataFrame, file_path: str) -> None:
        dataframe.to_csv(file_path, sep=self.separator, index=False)
