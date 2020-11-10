# import pandas as pd
# import numpy as np


def query_order_by(x):
    _query = ''
    if isinstance(x, str):
        if x == '':
            _query = ''
        else:
            _query = f'ORDER BY {x}'
    elif isinstance(x, list):
        list_x = str(x).replace('[', '(').replace(']', ')')
        _query = f'ORDER BY {list_x}'
    else:
        raise TypeError('Only String or List Data Types are Accepted')
    return _query


def query_partition_by(x):
    _query = ''
    if isinstance(x, str):
        if x == '':
            _query = ''
        else:
            _query = f'PARTITION BY {x}'
    elif isinstance(x, list):
        list_x = str(x).replace('[', '(').replace(']', ')')
        _query = f'PARTITION BY {list_x}'
    else:
        raise TypeError('Only String or List Data Types are Accepted for partition by')
    return _query


def query_sample_by(x):
    _query = ''
    if isinstance(x, str):
        if x != '':
            _query = f'SAMPLE BY {x}'
    elif isinstance(x, list):
        list_x = str(x).replace('[', '(').replace(']', ')')
        _query = f'SAMPLE BY {list_x}'
    else:
        raise TypeError('Only String or List Data Types are Accepted for sample by')
    return _query


def query_settings(x):
    _query = 'SETTINGS '
    if isinstance(x, str):
        if x == '':
            _query = ''
        else:
            _query = _query + x
    elif isinstance(x, list):
        for i in x:
            if i != x[-1]:
                _query = _query + i + ', '
            else:
                _query = _query + i
    else:
        raise TypeError('Only String or List Data Types are Accepted for Settings')
    return _query

def query_TTL(x):
    _query = 'TTL '
    if isinstance(x, str):
        if x == '':
            _query = ''
        else:
            _query = _query + x
    else:
        raise TypeError('Only String Data Types are Accepted for TTL')
    return _query

# if __name__ == '__main__':
#     query_order_by(x)
#     query_partition_by(x)

# xy = ['sdf', 'asdf']
# ab = ['index_granularity = 8129', 'sadfsdaf = asdfsd']
# das = {'dad': 'sd'}
# empt = 'sadas'
# print(query_partition_by(ab),query_order_by(ab))
# print(query_settings(ab))
# print('query is: ', query_settings(empt))
