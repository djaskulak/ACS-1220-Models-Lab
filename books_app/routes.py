"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from books_app.models import *

# Import app and db from events_app package so that we can run app
from books_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    # TODO: Make a query for all instances of 'User' and send to the template
    all_users = User.query.all()
    return render_template('home.html', all_users=all_users)

@main.route('/profile/<username>')
def profile(username):
    # TODO: Make a query for the user with the given username, and send to the
    # template
    user = User.query.filter_by(username=username).first()
    favorite_books = user.favorite_books
    return render_template('profile.html', username=username, books=favorite_books)
