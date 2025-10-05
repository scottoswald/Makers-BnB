import os
from flask import Flask, request, render_template, flash, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.space import Space 
from lib.user_repositiory import UserRepository
from lib.space_repository import SpaceRepository

def apply_userpage_routes(app):

    @app.route('/userpage', methods=['GET'])
    def userpage_display():

        connection = get_flask_database_connection(app)
        user_repo = UserRepository(connection)
        space_repo = SpaceRepository(connection)

        user_id = session.get('user_id')
        if not user_id:
            flash("Please log in.")
            return redirect('/')


        user = user_repo.find(user_id)
        user_spaces = space_repo.find_by_user_id(user_id)

        print("User ID from session:", user_id)
        print("User:", user.username)
        print("Spaces:", user_spaces)

        return render_template(
            'userpage.html',
            username=user.username,
            email=user.email,
            phone_number=user.phone_number,
            spaces=user_spaces
        )
    
    @app.route("/find_space", methods=["POST"])
    def find_space():
        return render_template("find_space.html")

    @app.route('/add_space', methods=['POST'])
    
    def add_space():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)

        name = request.form.get('name')
        if not name:
            flash("Name is required.")
            return redirect('/userpage')

        description = request.form['description']
        location = request.form['location']
        type = request.form['type']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        price_per_night = request.form['price_per_night']
        
        # Get user_id from session
        user_id = session.get('user_id')
        if not user_id:
            flash("You must be logged in to add a space.")
            return redirect('/')
        
        # Check if space with this name already exists for the user
        #existing_space = repository.find_by_name_and_user_id(name, user_id)
        #if existing_space:
         #   flash("You already have a space with this name. Please choose a different name.")
          #  return redirect('/userpage')

        # Description validation
        if len(description) > 100:
            flash("Description must be 100 characters or fewer.")
            return redirect('/userpage')

        # Price validation
        try:
            price_per_night = float(price_per_night)
            if price_per_night <= 0:
                raise ValueError
        except ValueError:
            flash("Price per night must be a positive number.")
            return redirect('/userpage')

        # All good – create space
        space = Space(None, name, description, location, type, start_date, end_date, price_per_night, user_id)
        repository.create(space)
        #print(f"Inserted space: {space.name}, {space.description}, {space.price_per_night}, user_id: {space.user_id}")

        return render_template('thankyou.html')
    

    @app.route('/spaces/<int:id>')
    def show_space(id):
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        space = repository.find(id)
        return render_template("listings.html", listings=[space])
    
    @app.route('/sign_out')
    def sign_out():
        session.clear()
        flash("You have signed out.")
        return redirect('/')
        