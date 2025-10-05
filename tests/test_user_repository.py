from lib.user_repositiory import UserRepository
from lib.user import User
from lib.database_connection import DatabaseConnection

def test_get_all(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'Dave', 'HelloWorld1!', 'dave@dave.com', '07123456789'),
        User(2, 'Karen', 'HelloWorld2!', 'karen@dave.com', '07987654321'),
        User(3, 'Scott', 'HelloWorld3!', 'scott@dave.com', '07067543278'),
        User(4, 'John', 'HelloWorld4!', 'john@dave.com', '07984386385'),
    ]

def test_find_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    users = repository.find(1)
    assert users == User(1, 'Dave', 'HelloWorld1!', 'dave@dave.com', '07123456789')

def test_create_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    repository.create(User(None, 'Sam', 'Password1!', 'sam@sam.com', '07129834765'))
    assert repository.all() == [
        User(1, 'Dave', 'HelloWorld1!', 'dave@dave.com', '07123456789'),
        User(2, 'Karen', 'HelloWorld2!', 'karen@dave.com', '07987654321'),
        User(3, 'Scott', 'HelloWorld3!', 'scott@dave.com', '07067543278'),
        User(4, 'John', 'HelloWorld4!', 'john@dave.com', '07984386385'),
        User(5, 'Sam', 'Password1!', 'sam@sam.com', '07129834765')
    ]
    
def test_delete_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
        User(2, 'Karen', 'HelloWorld2!', 'karen@dave.com', '07987654321'),
        User(3, 'Scott', 'HelloWorld3!', 'scott@dave.com', '07067543278'),
        User(4, 'John', 'HelloWorld4!', 'john@dave.com', '07984386385'),
    ]