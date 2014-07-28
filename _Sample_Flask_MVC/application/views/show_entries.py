from flask import render_template
from application import app

@app.route('/')
def show_entries():
    return render_template('show_entries.html')