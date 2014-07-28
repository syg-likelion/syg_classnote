from flask import render_template
from application import app
from application.models import data_manager

@app.route('/userpage')
def userpage():
	accounts = data_manager.load_account()
	return render_template('userpage.html', data = accounts)