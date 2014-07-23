import os
from flask import Flask, render_template, request
from stress import process_text

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def main():
    if request.method == 'POST' and len(request.form['text'].strip()):
        return render_template('response.html',
                               stressed=process_text(request.form['text']))
    return render_template('form.html')


