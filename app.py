# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:13:06 2022

@author: HP
"""

from flask import Flask, redirect, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    
    return  render_template('html.final project.html')

@app.route('/login')
def login():
    
    return render_template('login.html')

@app.route('/buy')
def buy():
    
    return render_template('buy.html')

@app.route('/rent')
def rent():
    
    return render_template('rent.html')

@app.route('/registration')
def registration():
    
    return render_template('registration.html')



app.run()
