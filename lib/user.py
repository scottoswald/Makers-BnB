class User():
    def __init__(self, id, username, password, email, phone_number):
        self.id = id
        self.username = username 
        self.password = password
        self.email = email 
        self.phone_number = phone_number
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    @staticmethod
    def password_suitable(password):
        special_char = "!@£$%&*?."
        numbers = "0123456789"
        if (
            len(password) < 8 or
            not any(char in special_char for char in password) or
            not any(char in numbers for char in password)
        ):
            return False
        else:
            return True

    @staticmethod
    def phone_number_suitable(phone_number):
        if len(phone_number) != 11 or not phone_number.startswith('07'):
            return False
        else:
            return True
            
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.password}, {self.email}, {self.phone_number})"
    