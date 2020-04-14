"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from seanproject import app
from seanproject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64
import os

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError

from seanproject.Models.QueryFormStracture import QueryFormStructure 
from seanproject.Models.QueryFormStracture import LoginFormStructure
from seanproject.Models.QueryFormStracture import UserRegistrationFormStructure 

csvFolder = os.path.dirname(os.path.abspath("psGames.csv"))
print(f'csvFolder={csvFolder}')
csvPath = os.path.join(csvFolder, 'psGames.csv')
print(f'csvPath={csvPath}')

db_Functions = create_LocalDatabaseServiceRoutines()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            return redirect('/login')
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('/queri')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )


df = pd.read_csv("C:\\Users\\User\\source\\repos\\seanproject\\seanproject\\seanproject\\static\\data\\psGames (1).csv")
@app.route  ('/dataSet')
def dataSet():
    """Renders the about page."""
    return render_template(
        'dataSet.html',
        title='dataSet',
        year=datetime.now().year,
        message='My Data Set', data = df.to_html(classes = "table table-hover")
    )
@app.route('/data')
def data():
    """Renders the contact page."""
    return render_template(
        'data.html',
        title='data',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/queri')
def queri():
    """Renders the about page."""
    return render_template(
        'queri.html',
        title='Queri',
        year=datetime.now().year,
        message='My Queri'
    )