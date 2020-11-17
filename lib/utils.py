import csv
import pandas as pd
# import pprint
import pkgutil


class Extractor:
    def __init__(self, file):
        self.file = file

    @classmethod
    def txt_to_df(cls, packages, path):
        file = pkgutil.get_data(packages, path).decode('utf-8')
        data = pd.DataFrame([line.split('\t') for line in file.split('\r\n')])
        data = data.rename(columns=data.iloc[0]).drop(data.index[0]).set_index('name')
        return cls(data)

    @classmethod
    def txt_to_dict(cls, packages, path):
        file = pkgutil.get_data(packages, path).decode('utf-8')
        data = pd.DataFrame([line.split('\t') for line in file.split('\r\n')])
        data = data.rename(columns=data.iloc[0]).drop(data.index[0]).set_index('name')
        dict_data = data.T.to_dict()
        # newdict = {}
        # for x in dict_data:
        #     new_key = f"{dict_data[x]['database']}.{dict_data[x]['table']}.{dict_data[x]['name']}"
        #     newdict[new_key] = dict_data[x]
        return cls(dict_data)
