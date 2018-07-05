import os
from datetime import datetime
from flask import Flask, redirect, render_template, request


# Flask setup
app = Flask(__name__)

messages = []


# Add messages method
def add_messages(username, message):
    """Adds and stores messages for each user"""
    current_time = datetime.now().strftime("%H:%M:%S")
    message_dict = {"timestamp":current_time, "username":username, "message":message }
    messages.append(message_dict)
    # messages.append("( {} ) {} : {}".format(current_time, username, message))
    
    
# Get messages method
def get_messages():
    """Returns all messages in a readable format for a user"""
    return messages


# Base view
@app.route("/", methods = ["GET", "POST"])

## Base method
def index():
    """Contains the instructions for using the application"""
    if request.method == "POST":
        with open("data/users.txt", "a+") as user_list:
            user_list.write(request.form["username"] + "\n")
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