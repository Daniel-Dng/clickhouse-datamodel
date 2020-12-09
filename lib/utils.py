import re


def query_add_func(obj, func):
    _query = ''
    if isinstance(obj, str):
        if obj != '':
            _query = f"{func}({obj})"
    elif isinstance(obj, list):
        _list_obj = ','.join(obj)
        _query = f"{func}({_list_obj})"
    return _query


def query_rmv_func(obj_with_func):
    if (obj_with_func != '') & ('(' in obj_with_func) & (')' in obj_with_func):
        obj = re.findall('\((.*)\)', obj_with_func)[0]
        func = re.findall('(.*)\(', obj_with_func)[0]
    return obj, func

# print(query_rmv_func('func(nullable(obj))'))
# TODO: need opti


def query_order_by(x):
    _query = ''
    if isinstance(x, str):
        if x.strip() != '':
            _query = f'ORDER BY ({x})'
        else:
            _query = ''
    elif isinstance(x, list):
        list_x = ','.join(x)
        _query = f'ORDER BY ({list_x})'
    else:
        raise TypeError('Only String or List Data Types are Accepted for order_columns')
    return _query


def pri_key(x):
    _query = ''
    if isinstance(x, str):
        if x == '':
            _query = ''
        else:
            _query = f'PRIMARY KEY ({x})'
    elif isinstance(x, list):
        list_x = ','.join(x)
        _query = f'PRIMARY KEY ({list_x})'
    else:
        raise TypeError('Only String or List Data Types are Accepted for Primary Key')
    return _query


def query_partition_by(x):
    _query = ''
    if isinstance(x, str):
        if x != '':
            _query = f'PARTITION BY ({x})'
    elif isinstance(x, list):
        list_x = ','.join(x)
        _query = f'PARTITION BY ({list_x})'
    else:
        raise TypeError('Only String or List Data Types are Accepted for partition_columns')
    return _query


def query_sample_by(x):
    _query = ''
    if isinstance(x, str):
        if x != '':
            _query = f'SAMPLE BY ({x})'
    elif isinstance(x, list):
        list_x = ','.join(x)
        _query = f'SAMPLE BY ({list_x})'
    else:
        raise TypeError('Only String or List Data Types are Accepted for sample_columns')
    return _query


def query_settings(x):
    _query = ''
    if isinstance(x, str):
        if x != '':
            _query = 'SETTINGS ' + x
    elif isinstance(x, list):
        _query = 'SETTINGS ' + ','.join(x)
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


def query_prikey(x):
    _query = ''
    if isinstance(x, str):
        if x == '':
            _query = ''
        else:
            _query = f'PRIMARY KEY ({x})'
    elif isinstance(x, list):
        list_x = ','.join(x)
        _query = f'PRIMARY KEY ({list_x})'
    else:
        raise TypeError('Only String or List Data Types are Accepted for primary_keys')
    return _query


def query_columns(col, data_type, function=''):
    _query = ''
    data_type = data_type.strip()
    col = col.strip()
    function = function
    if function != '':
        data_type = query_add_func(data_type, function)
    if isinstance(col, str):
        _query = _query + col + ' ' + data_type
    # elif isinstance(col, list) & isinstance(data_type, list):
    #     pd.DataFrame(columns=['col','data_type'],data=)
    else:
        raise TypeError('Only String or List data types are accepted for columns')
    return _query
