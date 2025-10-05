from flask import request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository 
from lib.space import Space 

def apply_find_space_routes(app):

    @app.route('/find_space', methods=['GET'])
    def find_space_form():
        return render_template('find_space.html')
    

    @app.route('/find_space', methods=['POST'])
    def find_space_results():
        location = request.form['location']
        space_type = request.form['type']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        price_min = request.form['price_min']
        price_max = request.form['price_max']

        connection = get_flask_database_connection(app)
        repo = SpaceRepository(connection)
        listings = repo.search(location, space_type, start_date, end_date, price_min, price_max)

        return render_template('listings.html', listings=listings)

    
    
    # @app.route('/search_spaces', methods=['POST'])
    # def search_spaces_results():
    #     connection = get_flask_database_connection(app)
        #repository = SpaceRepository(connection)
        #search_query = request.form.get('search_query', '').strip() # Get search query from form


# --- SIMULATE SPACE REPOSITORY DATA ---
#all_mock_spaces = [
#Space(id=1, name="Cozy City Apartment", description="A charming apartment in the heart of the city, perfect for solo travelers.", price_per_night=120.00, user_id=1),
#Space(id=2, name="Spacious Family Home", description="Perfect for a large family, with a big garden and outdoor play area.", price_per_night=350.50, user_id=2)
#]

#found_spaces = [] # Initialize empty list for results
