from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM spaces")
        # Update to match new Space constructor and column names
        return [Space(row["id"], row["name"], row["description"], row["location"], row["type"], row["start_date"], row["end_date"], row["price_per_night"], row["user_id"]) for row in rows]

    def find(self, id):
        rows = self.connection.execute("SELECT * FROM spaces WHERE id = %s", [id])
        row = rows[0]
        # Update to match new Space constructor and column names
        return Space(row["id"], row["name"], row["description"], row["location"], row["type"], row["start_date"], row["end_date"], row["price_per_night"], row["user_id"])
    
        
    def find_by_user_id(self, user_id):
        rows = self.connection.execute("SELECT * FROM spaces WHERE user_id = %s", [user_id])
        return [Space(row["id"], row["name"], row["description"], row["location"], row["type"], row["start_date"], row["end_date"], row["price_per_night"], row["user_id"]) for row in rows]

    def create(self, space):
        # Update to insert into 'spaces' table with new columns
        self.connection.execute(
            "INSERT INTO spaces (name, description, location, type, start_date, end_date, price_per_night, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            [space.name, space.description, space.location, space.type, space.start_date, space.end_date, space.price_per_night, space.user_id]
        )
        return None

    def search(self, location, space_type, start_date, end_date, price_min, price_max):
        # Update to query 'spaces' table and use correct column names
        rows = self.connection.execute(
            """
            SELECT * FROM spaces
            WHERE location ILIKE %s
            AND type ILIKE %s
            AND start_date <= %s
            AND end_date >= %s
            AND price_per_night BETWEEN %s AND %s
            """,
            [f"%{location}%", f"%{space_type}%", start_date, end_date, price_min, price_max]
        )
        # Update to match new Space constructor and column names
        return [Space(row["id"], row["name"], row["description"], row["location"], row["type"], row["start_date"], row["end_date"], row["price_per_night"], row["user_id"]) for row in rows]