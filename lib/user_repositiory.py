from lib.user import User
class UserRepository():
    
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['id'], row['username'], row['password'], row['email'], row['phone_number'])
            users.append(item)
        return users
    
    def find(self, id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s', [id])
        row = rows[0]
        return User(row['id'], row['username'], row['password'], row['email'], row['phone_number'])
    
    def create(self, user):
        self.connection.execute('INSERT INTO users (username, password, email, phone_number) VALUES(%s, %s, %s, %s)', [user.username, user.password, user.email, user.phone_number])
        return None
    
    def delete(self, id):
        self.connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None
    
    def find_by_username(self, username):
        rows = self.connection.execute(
        'SELECT * FROM users WHERE username = %s', [username]
        )
        if not rows:
            return None
        row = rows[0]
        return User(row['id'], row['username'], row['password'], row['email'], row['phone_number'])
    
    def find_by_email(self, email):
        rows = self.connection.execute(
        'SELECT * FROM users WHERE email = %s', [email]
        )
        if not rows:
            return None
        row = rows[0]
        return User(row['id'], row['username'], row['password'], row['email'], row['phone_number'])