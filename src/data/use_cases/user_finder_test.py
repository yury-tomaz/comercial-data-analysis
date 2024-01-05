from src.infra.db.tests.users_repository import UsersRepositorySpy
from src.data.use_cases.user_finder import UserFinder

def test_user_finder():
    first_name = 'yury'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

 
    assert repo.select_user_attributes["first_name"] == first_name

    assert response['type'] == 'users'
    assert response['count'] == len(response["atributes"])
    assert response["atributes"] != []


def test_user_finder_with_empty_list():
    first_name = 'yury1121'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Invalid first name'