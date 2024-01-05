from abc import ABC, abstractmethod
from typing import List
from src.domain.entity.user import User

class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None: pass
    
    @abstractmethod
    def select_user(self, first_name: str) -> list[User]: pass