import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DbConnectionHandle
from .users_repository import UsersRepository

db_connection_handle = DbConnectionHandle()
connection = db_connection_handle.get_engine().connect()

@pytest.mark.skip(reason='Sensive test')
def test_insert_user():
    mocked_first_name = 'valid_name'
    mocked_last_name = 'valid_last_name'
    mocked_age = 34

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql = '''
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = {}
    '''.format(mocked_first_name, mocked_last_name, mocked_age)

    response = connection.execute(text(sql))
    registery = response.first()

    assert registery.first_name == mocked_first_name
    assert registery.last_name == mocked_last_name
    assert registery.age == mocked_age

    # Agora, exclua o registro

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registery.id}
    '''))
    connection.commit()

def test_select_user():
    sql = '''
        INSERT INTO users (first_name, last_name, age)
        VALUES ('valid_name', 'valid_last_name', 34)
    '''
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user('valid_name')

    assert response[0].first_name == 'valid_name'
    assert response[0].last_name == 'valid_last_name'
    assert response[0].age == 34

    # Agora, exclua o registro

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
    '''))
    connection.commit()