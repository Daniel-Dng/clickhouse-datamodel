from lib.functions import query_add_func
from lib.objects import Tables


class Columns(Tables):
    def __init__(self, col_name, data_type, nullable=0, function='', codec= ''):
        self.col_name = col_name
        self.function = function
        self.codec = codec
        self.nullable = nullable
        self.data_type = data_type if nullable == 0 else query_add_func(data_type, 'Nullable')
        self.data_type = self.data_type if function == '' else query_add_func(self.data_type, function)

    def __str__(self):
        return f"{self.col_name} " \
               f"{self.data_type} " \
               f"{self.codec}"

    def add_function(self, function):
        if self.function == '':
            self.data_type = query_add_func(self.data_type, function)
        else:
            raise SyntaxError('The data type already has a function')
        return self

    def add_codec(self, codec):
        self.codec = self.codec + 'CODEC(' + codec + ')'
        return self


# class Prikey(Tables.Columns):
#     def __init__(self, name, datatype, function='', is_in_primary_key=0, is_in_sorting_key=0,
#                  is_in_partition_key=0, compression_codec='', is_in_sampling_key=0):
#         super().__init__(name, datatype, function, 1, 1,
#                          is_in_partition_key, compression_codec, is_in_sampling_key)




# test = Columns('ps_name', 'String').add_function('LowCardinality').add_codec('Default')
# test2 = Columns('ps_id', 'UInt8', 0).add_function('LowCardinality').add_codec('Default')
# test3 = Columns('ps_id', 'UInt8', 0).add_function('Hash').add_codec('Default')
# print(test, test3)

# tab = Tables('payment_systems', 'entities', 'MergeTree').add_columns('   ps_ndames',' String')
# tab2 = tab.add_columns(str(test2))
# print(tab)
# print(tab2)
# print(test2)
