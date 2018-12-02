from flask import Flask, request, send_file
from walmart import pathfind
app = Flask(__name__)


@app.route('/')
def indexhtml():
    return send_file('./public/index.html')


@app.route('/js/index.js')
def indexjs():
    return send_file('./public/js/index.js')


@app.route('/css/index.css')
def indexcss():
    return send_file('./public/css/index.css')


@app.route('/submit')
def handleSubmit():
    categories = request.args.get('list').split(',')
    pathfind(categories)
    return send_file('path.png')
