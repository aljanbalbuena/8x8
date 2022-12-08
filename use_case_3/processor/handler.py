from processor import DataProcessor, FileProcessor


class Init:
    def __init__(self, input_a: str, input_b: str, col_name: str, output: str):
        """
        Initialize necessary process details

        :param input_a:
            Path of first file input
        :param input_b:
            Path of second file input
        :param col_name:
            Column where to merge the two input
        :param output:
            Path to output file
        """
        self.fp = FileProcessor()
        self.dp = DataProcessor()
        self.input_a = input_a
        self.input_b = input_b
        self.col_name = col_name
        self.output = output

    def run(self):
        # Load input csv files content to tables
        df_a = self.fp.read_csv(self.input_a)
        df_b = self.fp.read_csv(self.input_b)

        # Merge tables on common column
        merged_data = self.dp.merge(df_a, df_b, self.col_name)

        # Write merged data to csv
        self.fp.write_csv(merged_data, self.output)
