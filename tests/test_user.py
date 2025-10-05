from lib.user import User

def test_user_initialises():
    user = User(1, 'Dave', 'StellaArtois1!', 'dave@dave.com', '07123456789')
    assert user.id == 1
    assert user.username == 'Dave'
    assert user.password == 'StellaArtois1!'
    assert user.email == 'dave@dave.com'
    assert user.phone_number == '07123456789'

def test_users_are_equal():
    user1 = User(1, 'Dave', 'StellaArtois1!', 'dave@dave.com', '07123456789')
    user2 = User(1, 'Dave', 'StellaArtois1!', 'dave@dave.com', '07123456789')
    assert user1 == user2

def test_users_formatted():
    user = User(1, 'Dave', 'StellaArtois1!', 'dave@dave.com', '07123456789')
    assert str(user) == "User(1, Dave, StellaArtois1!, dave@dave.com, 07123456789)"


def test_password_too_short():
    assert not User.password_suitable("Ab1!")

def test_password_missing_number():
    assert not User.password_suitable("Password!")

def test_password_missing_special():
    assert not User.password_suitable("Password1")

def test_password_valid():
    assert User.password_suitable("StrongPass1!")


def test_phone_too_short():
    assert not User.phone_number_suitable("07123")

def test_phone_wrong_start():
    assert not User.phone_number_suitable("06123456789")

def test_phone_too_long():
    assert not User.phone_number_suitable("07123456789123")

def test_valid_phone_number():
    assert User.phone_number_suitable("07123456789")