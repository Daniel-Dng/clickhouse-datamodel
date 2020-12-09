from lib.utils import query_add_func
from lib.tables import Tables


class Columns(Tables):
    def __init__(self, col_name, data_type, nullable=0, function='', codec=''):
        self.col_name = col_name
        self.function = function
        self.codec = 'CODEC(' + codec + ')' if codec != '' else codec
        self.nullable = nullable
        self.data_type = data_type if nullable == 0 else query_add_func(data_type, 'Nullable')
        self.data_type = self.data_type if function == '' else query_add_func(self.data_type, function)

    def __str__(self):
        return f"{self.col_name} " \
               f"{self.data_type} " \
               f"{self.codec} "

    def add_function(self, function):
        if self.function == '':
            self.data_type = query_add_func(self.data_type, function)
        else:
            raise SyntaxError('The data type already has a function')
        return self

    def add_codec(self, codec):
        self.codec = self.codec + 'CODEC(' + codec + ')'
        return self
