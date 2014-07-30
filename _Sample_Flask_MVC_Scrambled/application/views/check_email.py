# 후후 수고가 많다.
@app.route('/check_email', methods=['POST'])
def check email():
    if request.method == 'POST':
        data_manager.load_account()
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
