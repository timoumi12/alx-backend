#!/usr/bin/env python3
'''task0'''
from flask import Flask, render_template


app = Flask(__name__, static_url_path='')


@app.route('/', strict_slashes=False)
def index():
    '''returns 0-index.html'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
