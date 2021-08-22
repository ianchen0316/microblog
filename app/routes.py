from flask import render_template
from app import application

@application.route('/')
@application.route('/index')
def index():

    # Mock data
    user = {'username' : 'Miguel'}

    return render_template('index.html', title='Home', user=user)
