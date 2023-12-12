from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import test

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/findID', methods=['POST'])
def findIDFunc():
    text_input = request.form['text']
    # Run your function here with text_input
    result = test.findID(text_input)  # call the function from the other file
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)