from flask import request, render_template, redirect
from application import app
from application.models import data_manager
import json

@app.route('/check_email', methods=['GET', 'POST'])
def check_email():
    if request.method == 'POST':
        accounts = data_manager.load_account()
        result = {}
        result['message'] = 'ok'
        for account in accounts :
            if account['email'] == request.form['email'] :
                result['message'] = 'error'
                break
        return json.dumps(result)
    else :
        message = 'try it again'
    return render_template('signup.html', message = message)
