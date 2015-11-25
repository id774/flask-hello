# -*- coding: utf-8 -*-

import sys
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Routing
@app.route('/')
def form():
    return render_template('form_submit.html')

@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html',
                           name=name, email=email)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
