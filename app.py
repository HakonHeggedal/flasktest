#!/usr/bin/python
# coding: utf-8
import flask

app = flask.Flask(__name__)


@app.route('/')
def entry_point():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
