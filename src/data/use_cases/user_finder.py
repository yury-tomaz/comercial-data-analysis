from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository_interface import UsersRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, user_repo: UsersRepositoryInterface):
        self._user_repo = user_repo

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)

        users = self.__search_user(first_name)

        return self.__format_response(users)

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise Exception('Invalid first name')
        
        if len(name) > 18:
            raise Exception('Name must be less than 18 characters')
        
        return True
    
    def __search_user(self, first_name: str) -> list:
        users = self._user_repo.select_user(first_name)
        if(users == []): raise Exception('User not found')
        return users
    
    @classmethod
    def __format_response(cls, users: List[Dict]) -> Dict:
        attributes = []

        for user in users:
            attributes.append({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age
            })

        response = {
            "type": "users",
            "count": len(users),
            "atributes": attributes
        }
        return response