import os
import markdown
from flask import Flask, render_template, request, Markup
from stress import process_text

app = Flask(__name__)

def process_and_markdown(text):
    # 1. run process_text and get stressed output
    # 2. insert two spaces before newlines so that lines are maintained
    # 3. run through markdown
    return Markup(markdown.markdown(
                  process_text(request.form['text']).replace("\n", "  \n")))

@app.route('/', methods=['POST','GET'])
def main():
    if request.method == 'POST' and len(request.form['text'].strip()):
        return render_template('response.html',
                               stressed=process_and_markdown(request.form['text']))
    return render_template('form.html')


