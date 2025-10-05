from flask import request, render_template, redirect, flash
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space # Make sure lib.space is updated

def apply_booking_routes(app):

    @app.route('/find_space', methods=['GET'], endpoint='show_search_form')
    def show_search_form():
        return render_template('find_space.html')  

    @app.route('/find_space', methods=['POST'], endpoint='handle_find_space')
    def find_space_page():
        location = request.form.get('location')
        space_type = request.form.get('type') # Renamed from 'type' to 'space_type' to avoid conflict with Python's built-in type
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        price_min = request.form.get('price_min')
        price_max = request.form.get('price_max')

        
        if not all([location, space_type, start_date, end_date, price_min, price_max]):
            flash("Please fill out all fields.")
            return render_template('find_space.html')

        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        
        # Pass space_type to the search method
        results = repository.search(location, space_type, start_date, end_date, price_min, price_max)

        if not results:
            flash("No listings found matching your criteria.")
            return render_template('find_space.html')

        return render_template('listings.html', listings=results)

