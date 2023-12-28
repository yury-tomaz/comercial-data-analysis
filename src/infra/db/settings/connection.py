from sqlalchemy import create_engine

class DbConnectionHandle:
  def __init__(self) -> None:
    self._connection_string = "{}://{}:{}@{}:{}/{}".format(
     'mysql+pymysql',
      'root',
      '',
      'localhost',
      '3306',
      'clean_database'
    )
    self.__engine = self.__crete_database_engine()
    
  def __crete_database_engine(self):
    engine = create_engine(self._connection_string)
    return engine
  
  def get_engine(self):
    return self.__engine
    