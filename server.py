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

@app.route('/case1')
def case1():
    return render_template('case1.html')  # Create a case1.html template

@app.route('/case2')
def case2():
    return render_template('case2.html')  # Create a case2.html template

@app.route('/case3')
def case3():
    return render_template('case3.html')  # Create a case3.html template

@app.route('/case4')
def case4():
    return render_template('case4.html')

@app.route('/resources')
def contact():
    return render_template('resources.html')

@app.route('/ahead')
def ahead():
    return render_template('ahead.html')


if __name__ == '__main__':
   app.run(debug = True)