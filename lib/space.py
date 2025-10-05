class Space:
    def __init__(self, id, name, description, location, type, start_date, end_date, price_per_night, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.price_per_night = price_per_night
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.location}, {self.type}, {self.start_date}, {self.end_date}, {self.price_per_night}, {self.user_id})"



    # # I know the below looks needlessly complex! But the normal __eq__ funcion above
    # # doesn't like floats, and we need them for currency

    # def __eq__(self, other):
    #     if not isinstance(other, Space):
    #         return False
    #     return (
    #         self.id == other.id and
    #         self.name == other.name and
    #         self.description == other.description and
    #         float(self.price_per_night) == float(other.price_per_night) and
    #         self.user_id == other.user_id
    #     )
    
    # def __repr__(self):

    #     return f"Space({self.id}, {self.name}, {self.description}, {self.price_per_night:.2f}, {self.user_id})"
    
    # #     # --- Validation Methods ---
    # # @staticmethod
    # # def name_suitable(name):
    # #     """
    # #     Validates if the space name is suitable (e.g., between 3 and 100 characters).
    # #     """
    # #     return 3 <= len(name) <= 100

    # # @staticmethod
    # # def description_suitable(description):
    # #     """
    # #     Validates if the space description is suitable (e.g., between 10 and 500 characters).
    # #     """
    # #     return 10 <= len(description) <= 500

    # # @staticmethod
    # # def price_per_night_suitable(price_per_night):
    # #     """
    # #     Validates if the price_per_night is a positive number.
    # #     Accepts string input for easier form processing.
    # #     """
    # #     try:
    # #         price_float = float(price_per_night)
    # #         return price_float > 0
    # #     except ValueError:
    # #         return False

