from flask import request, render_template
from application import app
from application.models import data_manager
import re

@app.route('/signup', methods=['GET', 'POST'])
def signup() :
    if 'admin' in request.form :
        admin = True
    else :
        admin = False
    message = None

    if request.method == 'POST' :
        if request.form['email'] == '' :
            message = 'Please fill out your email'
        elif request.form['pw'] == '' :
            message = 'Please fill out password'
        else :
            if bool(re.search('[\w\d._]+@[\w\d-]+\.(com|net|co.kr)', request.form['email'])) :
                message = 'Valid email'
                if bool(re.search('(?=.{8,20})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!#\$%&\?])', request.form['pw'])) :
                    message = 'Valid password'
                    if request.form['pw']==request.form['pw_check'] :
                        accounts = data_manager.load_account()

                        account_info = {
                            'email' : request.form['email'],
                            'pw' : request.form['pw'],
                            'admin' : admin
                        }
                        for account in accounts :
                            if account['email'] == request.form['email'] :
                                message = 'Email already taken'
                                return render_template('signup.html', message = message)
                        else :
                            accounts.append(account_info)
                            data_manager.save_account(accounts)
                    else :
                        message = 'You should enter same password'
                else :
                    message = 'Invalid password format'
            else : 
                message = 'Inavalid email format'
    return render_template('signup.html', message = message)