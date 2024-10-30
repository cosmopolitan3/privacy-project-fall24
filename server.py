from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import url_for
from flask import session


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')  

@app.route('/cases')
def services():
    return render_template('cases.html') 

@app.route('/resources')
def contact():
    return render_template('resources.html')


if __name__ == '__main__':
   app.run(debug = True)