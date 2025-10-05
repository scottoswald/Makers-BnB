import os
from flask import Flask, request, render_template, flash, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repositiory import UserRepository
from lib.user import User

def apply_user_routes(app):
    
    @app.route('/create_account', methods=['GET'])
    def show_create_account_form():
        return render_template('create_account.html')

    # @app.route('/create_account', methods=['POST'])
    # def create_account():
    #     connection = get_flask_database_connection(app)
    #     repository = UserRepository(connection)
    #     password = request.form['password']
    #     if not User.password_suitable(password):
    #         flash("Password must be at least 8 characters long and include a number and a special character.")
    #         return render_template('create_account.html')
    #     phone_number = request.form['phone_number']
    #     if not User.phone_number_suitable(phone_number):
    #         flash("phone number must be 11 numbers and start with 07")
    #         return render_template('create_account.html')
    #     user = User(None, request.form['username'], password, request.form['email'], phone_number)
    #     user = repository.create(user)
    #     return redirect('/')

    @app.route('/create_account', methods=['POST'])
    def create_account():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        username = request.form['username']
        if repository.find_by_username(username):
            flash("Username already in use. Please choose another.")
            return render_template('create_account.html')
        password = request.form['password']
        if not User.password_suitable(password):
            flash("Password must be at least 8 characters long and include a number and a special character.")
            return render_template('create_account.html')
        email = request.form['email']
        if repository.find_by_email(email):
            flash("Email already in use.")
            return render_template('create_account.html')
        phone_number = request.form['phone_number']
        if not User.phone_number_suitable(phone_number):
            flash("phone number must be 11 numbers and start with 07")
            return render_template('create_account.html')
        user = User(None, username, password, email, phone_number)
        user = repository.create(user)
        return redirect('/')
