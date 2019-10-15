#!/usr/bin/python3.6
from flask import Flask
run= Flask(__name__) # flask constructor

@run.route('/') #route of page.
def request(): # create a function of responce
    return 'This is first app !!!!!!!!!!'

@run.route('/welcome')
def Index():
    return 'Welcome to Python class !!!!!!!!!!'

#@run.route('/web')
#{% include 'index.html' %}

run.run(debug =True) # run the application and enable to debug mode
