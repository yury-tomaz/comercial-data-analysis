from typing import List
from src.infra.db.settings.connection import DbConnectionHandle 
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository_interface import UsersRepositoryInterface
from src.domain.entity.user import User

class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DbConnectionHandle() as db_connection:
            try:
                new_user = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()

            except Exception as exception:
                db_connection.session.rollback()
                raise exception
            
    @classmethod
    def select_user(cls, first_name: str) -> List[User]:
        with DbConnectionHandle() as db_connection:
            try:
                user = (
                    db_connection.session
                    .query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                    )
                return user

            except Exception as exception:
                db_connection.session.rollback()
                raise exception