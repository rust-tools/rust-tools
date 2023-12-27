from flask import Flask, render_template, request
import pythonFunctions
import os
from appSettings import useLegacy, debugMode

# Declare proper settings
if useLegacy:
    print("Using legacy UI")
    use_template = "index_legacy.html"
elif useLegacy == False:
    print("Using new UI")
    use_template = "index.html"

# Declares the app variable to start the webapp
app = Flask(__name__)

# Renders the index.html page with the result variable. If the request method is POST, it will run the pythonFunctions.findDurability function and return the result to the index.html page
@app.route('/raidtool', methods=['GET', 'POST']) 
def home():
    if request.method == 'POST':
        input_data = request.form.get('getId')
        raidType = request.form.get('raidType')
        itemType = request.form.get('itemType')
        print(itemType, input_data, raidType)
        result = pythonFunctions.findDurability(itemType, input_data, raidType)
        return render_template('raidtool.html', result=result)
    return render_template('raidtool.html', result="waiting for input")

@app.route('/')
def index():
    return render_template(use_template)

@app.route('/home')
def homePage():
    return render_template(use_template)

# Runs the app
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)