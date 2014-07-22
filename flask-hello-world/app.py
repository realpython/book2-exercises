# --- Flask Hello World ---#

# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# dynamic route with an int type
@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

# dynamic route with an float type
@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"


# start the development server using the run() method
if __name__ == "__main__":
    app.run()
