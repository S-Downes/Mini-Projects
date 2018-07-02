import os
from flask import Flask


# Flask setup
app = Flask(__name__)


# Base view
@app.route("/")

## Base method
def index():
    """Contains the instructions for using the application"""
    return "<strong>To send a message use the following syntax:</strong> /USERNAME/MESSAGE"
    

# Username view
@app.route("/<username>")

## Username method
def user(username):
    """Provides a greeting to the user"""
    return "Hello and welcome " + username
    
    
# Message view
@app.route("/<username>/<message>")

## Message method
def message(username, message):
    """Allows the user to send messages"""
    return "{0} : {1}".format(username, message)
    
    
# Configuration
app.run(host = os.getenv("IP"), port = os.getenv("PORT"), debug = True)