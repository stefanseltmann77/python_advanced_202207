from pathlib import Path

from pyspark.sql import SparkSession


class DataAggregator:

    def __init__(self, input_path: Path, output_path: Path, ...):
        ...

    def aggregate(self, df, ...):
        ...

    def run(self) -> None:
        ...
        spark = SparkSession.builder.appName(self.spark_app_name).getOrCreate()
        ...
        raw_data_df = spark.read.parquet(self.input_path)
        ...
        aggregated_data = self.aggregate(df=raw_data_df, ...)
        ...
        aggregated_data.write.parquet(self.output_path, ...)
        ...
