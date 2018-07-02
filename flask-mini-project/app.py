import os
from flask import Flask, redirect


# Flask setup
app = Flask(__name__)

messages = []


# Add messages method
def add_messages(username, message):
    """Adds and stores messages for each user"""
    messages.append("{} : {}".format(username, message))
    
    
# Get messages method
def get_messages():
    """Returns all messages in a readable format for a user"""
    return "<br>".join(messages)


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
    """Provides a greeting to the user and uses get_messages() to return the messages for that user"""
    return "<h1>Hello and Welcome {0}</h1> {1}".format(username, get_messages())
    
    
# Message view
@app.route("/<username>/<message>")

## Message method
def message(username, message):
    """Allows the user to create and send messages and redirect to the chat page"""
    add_messages(username, message)
    return redirect(username)
    
    
# Configuration
app.run(host = os.getenv("IP"), port = os.getenv("PORT"), debug = True)