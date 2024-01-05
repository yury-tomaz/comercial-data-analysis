from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DbConnectionHandle:
    def __init__(self) -> None:
        self._connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            os.getenv('DB_USER', 'root'),
            os.getenv('DB_PASSWORD', 'root'),
            os.getenv('DB_HOST', 'localhost'),
            os.getenv('DB_PORT', '3306'),
            os.getenv('DB_NAME', 'clean_database')
        )
        self.__engine = self.__create_database_engine()
        self.Session = sessionmaker(bind=self.__engine)
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self._connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        self.session = self.Session() 
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        self.session.close()
        self.session = None
