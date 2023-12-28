from .connection import DbConnectionHandle

def test_crete_database_engine():
 db_connection_handle = DbConnectionHandle()
 
 engine = db_connection_handle.get_engine()
 
 assert engine is not None