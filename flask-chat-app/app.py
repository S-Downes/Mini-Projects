import os
from datetime import datetime
from flask import Flask, redirect, render_template, request


# Flask setup
app = Flask(__name__)


# Write to file method
def write_to_file(filename, data):
    """Opens a file in append mode and writes the contents of data to the file"""
    with open(filename, "a+") as file:
        file.writelines(data)
        
        
# Add messages method
def add_messages(username, message):
    """Adds and stores messages for each user in a text file called messages.txt"""
    write_to_file("data/messages.txt", "( {0} ) {1} - {2}\n".format(
            datetime.now().strftime("%H:%M:%S"),
            username.title(), 
            message))
    
    
# Get messages method
def get_messages():
    """Returns all messages in a readable format for a user by reading the messages.txt file and outputting this in chat.html"""
    messages = []
    with open ("data/messages.txt", "r+") as chat_messages:
        messages = chat_messages.readlines()
    return messages


# Base view
@app.route("/", methods = ["GET", "POST"])

## Base method
def index():
    """Method that Handles the POST request"""
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")
    
    
# Username view
@app.route("/<username>")

## Username method
def user(username):
    """Provides a greeting to the user and uses get_messages() to return the messages for that user"""
    messages = get_messages()
    return render_template("chat.html", username = username, chat_messages = messages)
    
    
# Message view
@app.route("/<username>/<message>")

## Message method
def message(username, message):
    """Allows the user to create and send messages and redirect to the chat page"""
    add_messages(username, message)
    return redirect(username)
    
    
# Configuration
app.run(host = os.getenv("IP"), port = os.getenv("PORT"), debug = True)