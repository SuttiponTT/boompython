import os
from flask import Flask, request, send_from_directory, url_for

app = Flask(__name__)

@app.route('/')
def index():
    print('Request for index page received')
    return "Hello World"

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        print('Request for hello page received with name=%s' % name)
        return f"Hello, {name}!"
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return "Hello World"

if __name__ == '__main__':
    app.run()
