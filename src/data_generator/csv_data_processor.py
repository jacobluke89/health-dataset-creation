from pyspark.errors import AnalysisException
from pyspark.sql import SparkSession, DataFrame


class CSVDataProcessor:

    def __init__(self, spark: SparkSession, file_path: str, sep: str = ','):
        self._spark = spark
        self.file_path = file_path
        self.sep = sep

    def _read_csv(self) -> DataFrame:
        """
        reads a csv file
        Returns:
            DataFrame: representing the csv file.
        """
        return self._spark.read.csv(self.file_path, sep=self.sep, inferSchema=True, header=True)

    @staticmethod
    def replace_spaces_in_column_headers(df: DataFrame) -> DataFrame:
        """
        Replace spaces with underscores in DataFrame column headers.

        Parameters:
        df (DataFrame): The DataFrame whose column headers need to be modified.

        Returns:
        DataFrame: A DataFrame with updated column headers.
        """

        new_columns = [c.replace(" ", "_").lower() for c in df.columns]

        return df.toDF(*new_columns)

    def runner(self) -> DataFrame | None:
        """
        Runs this class and returns a DataFrame representing the csv file
        Returns:
            DataFrame:
        """
        df = None
        try:
            df = self._read_csv()
        except AnalysisException as e:
            print(f"File, {self.file_path} not found, please check location thanks")
            print(f"Exception, {e}")
            return
        except Exception as e:
            print("Something went wrong running the csv file")
            print(e)
        return self.replace_spaces_in_column_headers(df)
