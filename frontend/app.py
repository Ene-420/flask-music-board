from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/library')

@app.route('/library')
def library():
    #response = requests.get('http://localhost:5000/library')
    #songs = response.json()

    return render_template('index.html', tracks={})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)