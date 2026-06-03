from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hi fuh u'

@app.route('/about')
def about():
    return 'About'
