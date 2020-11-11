import csv
import pandas as pd

class Extractor:
    def __init__(self, file):
        self.file = file
    @classmethod
    def csv_to_dict(cls, path):
        return cls(pd.read_csv(path, index_col='name').T.to_dict())

    @classmethod
    def csv_to_dict2(cls, path):
        with open(path, 'r') as file:
            data = []
            for line in csv.DictReader(file):
                data.append(line)
            file.close()
        return cls(data)
#
# sys_tab = Extractor.csv_to_dict2('../data/input_test.csv').file
# print(sys_tab)