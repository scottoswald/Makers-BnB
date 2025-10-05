from lib.space import Space

def test_space_initialises():
    space = Space(1, 'Buckingham Palace', 'A gorgeous location in the heart of town!', 100.00, 1)
    assert space.id == 1
    assert space.name == 'Buckingham Palace'
    assert space.description == 'A gorgeous location in the heart of town!'
    assert space.price_per_night == 100.00
    assert space.user_id == 1

def test_users_are_equal():
    space1 = Space(1, 'Buckingham Palace', 'A gorgeous location in the heart of town!', 100.00, 1)
    space2 = Space(1, 'Buckingham Palace', 'A gorgeous location in the heart of town!', 100.00, 1)
    assert space1 == space2

def test_users_formatted():
    space = Space(1, 'Buckingham Palace', 'A gorgeous location in the heart of town!', 100.00, 1)
    assert str(space) == "Space(1, Buckingham Palace, A gorgeous location in the heart of town!, 100.00, 1)"