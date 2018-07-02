import os
from flask import Flask


# Flask setup
app = Flask(__name__)


# Base view
@app.route("/")

## Base method
def index():
    return "<h2>Hello there!</h2>"
    
    
# Configuration
app.run(host = os.getenv("IP"), port = os.getenv("PORT"), debug = True)