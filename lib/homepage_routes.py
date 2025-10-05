import os
from flask import Flask, request, render_template, flash, redirect, session
from lib.database_connection import get_flask_database_connection , DatabaseConnection
from lib.user_repositiory import UserRepository
from lib.user import User

def apply_homepage_routes(app):
    
    @app.route("/", methods=["GET", "POST"])
    def login():
        connection = get_flask_database_connection(app)
        user_repo = UserRepository(connection)
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            user = user_repo.find_by_username(username)

            if not user or user.password != password:
                flash("Incorrect username or password")

                return redirect("/")
            session['user_id']=user.id
            
            return redirect("/userpage")

        return render_template("home.html")

