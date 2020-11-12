
import pandas as pd


class Extractor:
    def __init__(self, file):
        self.file = file

    @classmethod
    def csv_to_dict(cls, path):
        return cls(pd.read_csv(path, index_col= 'name').T.to_dict())

# print(type(Extractor.csv_to_dict('../data/table_engines.csv').file))

# print(Extractor.csv_to_dict('../data/table_engines.csv').file['View'])