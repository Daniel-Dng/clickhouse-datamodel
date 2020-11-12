import csv
import pandas as pd
import pprint

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources


template = pkg_resources.read_text(asset, 'input_test.csv')
print(template)
# or for a file-like stream:
# template = pkg_resources.open_text(templates, 'temp_file')

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
# input_test = Extractor.csv_to_dict2('../data/input_test.csv').file
# pprint.pprint(input_test[0])