import os
from flask import Flask, request, render_template, flash
from lib.database_connection import get_flask_database_connection
from lib.homepage_routes import apply_homepage_routes
from lib.user_routes import apply_user_routes




# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'i_dont_get_this'

with app.app_context():
    apply_homepage_routes(app) 
    apply_user_routes(app)

from lib.find_space_routes import apply_find_space_routes
apply_find_space_routes(app)

from lib.userpage_routes import apply_userpage_routes
apply_userpage_routes(app)

from lib.booking_routes import apply_booking_routes
apply_booking_routes(app)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
