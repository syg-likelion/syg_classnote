from flask import session, render_templates, redirect, url_for, flash
from application import app
from application.models.data_manager import *

@app.route('/login', methods=['GET','POST'])
def login(): 
    if request.method == 'POST':
        accounts = data_manager.load_account()
        print request.form
		for account in accounts :
            if account['email'] == request.form['email'] and account['pw'] == request.form['pw']:
                session['logged_in'] = True
                session['email'] = request.form['email']

                if account['admin'] :
                    session['admin'] = True
                else : 
                    session['admin'] = False

                return redirect(url_for('show_entries'))
        else
            message = 'Invalid email or password.'
    render_template('login.html', message = message)

@app.route('/logout')
def logout():
    flesh('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('admin', None)
    session.pop('email', None)
    flesh('You were logged out')
    return redirect(url_for('show_entries'))

