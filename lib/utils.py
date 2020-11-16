import csv
import pandas as pd
# import pprint
import pkgutil


class Extractor:
    def __init__(self, file):
        self.file = file

    # @classmethod
    # def csv_to_dict(cls, path):
    #     return cls(pd.read_csv(path, index_col='name').T.to_dict())
    #
    # @classmethod
    # def csv_to_dict2(cls, path):
    #     with open(path, 'r') as file:
    #         data = []
    #         for line in csv.DictReader(file):
    #             data.append(line)
    #         file.close()
    #     return cls(data)
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
        mydict = data.T.to_dict()
        # newdict = {}
        # for x in mydict:
        #     new_key = f"{mydict[x]['database']}.{mydict[x]['table']}.{mydict[x]['name']}"
        #     newdict[new_key] = mydict[x]
        return cls(mydict)


# sys_tab = Extractor.txt_to_dict('assets', 'table_engines.txt').file
#
# print(sys_tab['Kafka'])
