from typing import List
from src.domain.entity.user import User

class UsersRepositorySpy():

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes['first_name'] = first_name
        self.insert_user_attributes['last_name'] = last_name
        self.insert_user_attributes['age'] = age
        return
       
            
    def select_user(self, first_name: str) -> list[User]:
        self.select_user_attributes['first_name'] = first_name
        return [
            User(23, 'valid_name', 'valid_last_name', 99),
            User(24, 'valid_name', 'valid_last_name', 99),
            User(25, 'valid_name', 'valid_last_name', 99)
        ]