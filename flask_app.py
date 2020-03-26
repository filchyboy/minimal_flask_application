# flask_app.py - a minimal flsk application

# import flask module
from flask import Flask

# initiate application
app = Flask(__name__)


# define route
@app.route("/")
# attach a function to that route
def root():
    return("This is a minimally viable flask application. Git repo <a href='https://github.com/filchyboy/minimal_flask_application'>here</a>.")
