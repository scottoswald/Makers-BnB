from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.database_connection import DatabaseConnection

def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space(1, 'Buckingham Palace', 'A gorgeous location in the heart of town!', 100.00, 1),
        Space(2, 'The Natural History Museum', 'For the history buffs and taxidermy fans.', 200.00, 1),
        Space(3, 'Kensington Park', 'Very spacious and green. Perfect for a romantic getaway.', 250.00, 2),
        Space(4, 'The Tower of London', 'Very old. Very quaint. Lovely stuff.', 999.99, 3)
    ]

def test_find_space(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.find(1)
    assert spaces == Space(1, 'Buckingham Palace', 'A gorgeous location in the heart of town!', 100.00, 1)

def test_create_space(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = SpaceRepository(db_connection)
    repository.create(Space(None, 'Big Ben', 'Big clock. Cannot miss it', 100.00, 4))
    assert repository.all() == [
        Space(1, 'Buckingham Palace', 'A gorgeous location in the heart of town!', 100.00, 1),
        Space(2, 'The Natural History Museum', 'For the history buffs and taxidermy fans.', 200.00, 1),
        Space(3, 'Kensington Park', 'Very spacious and green. Perfect for a romantic getaway.', 250.00, 2),
        Space(4, 'The Tower of London', 'Very old. Very quaint. Lovely stuff.', 999.99, 3),
        Space(5, 'Big Ben', 'Big clock. Cannot miss it', 100.00, 4)
    ]
    
def test_delete_space(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = SpaceRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
        Space(2, 'The Natural History Museum', 'For the history buffs and taxidermy fans.', 200.00, 1),
        Space(3, 'Kensington Park', 'Very spacious and green. Perfect for a romantic getaway.', 250.00, 2),
        Space(4, 'The Tower of London', 'Very old. Very quaint. Lovely stuff.', 999.99, 3)
    ]