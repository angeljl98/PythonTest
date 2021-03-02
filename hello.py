from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola paníta'

# create an environment
# $ py -3 -m venv venv
#
# activate an environment
# > venv\Scripts\activate
# Your shell prompt will change to show
# the name of the activated environment.
#
# install Flask
# $ pip install Flask
#
#C:\path\to\app>set FLASK_APP=hello.py
#set FLASK_APP=hello.py
#python -m flask run
#* Running on http://127.0.0.1:5000/
