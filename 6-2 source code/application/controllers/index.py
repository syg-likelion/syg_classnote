#-*- coding:utf-8 -*-
from application import app
from flask import render_template, redirect, url_for, session


@app.route('/')
@app.route('/index')
def index() :
    if 'username' not in session:
        return redirect(url_for('sign'))
    else:
        return redirect(url_for('timeline'))

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404