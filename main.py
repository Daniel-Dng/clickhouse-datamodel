
# import db_connect as db
from lib.utils import Columns
from lib.utils import Tables

if __name__ =='__main__':
    col = Columns('ps_id','UInt8','YES','')
    print(col.name, col.data_type)
    print(col.to_query())
    print(Columns.attributes)
    print(Tables.attributes)


