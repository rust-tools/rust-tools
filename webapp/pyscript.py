from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable

#TODO: Flask tutorial kijken want ik heb dit lowkey gejat van internet en heb geen idee wat het doet