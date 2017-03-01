# imports
from flask import Flask, render_template

# configuration
DATABASE = ''
USERNAME = ''
PASSWORD = ''
SECRET_KEY = ''

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    text = "Hello, World!"
    return render_template('index.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
