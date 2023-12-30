from flask import Flask, render_template, session, request
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import os

import pythonFunctions
from appSettings import useLegacy, debugMode

# Declare proper settings
if useLegacy:
    print("[CONSOLE] Using legacy UI")
    use_template = "index_legacy.html"
elif useLegacy == False:
    print("[CONSOLE] Using new UI")
    use_template = "index.html"

# Declares the app variable to start the webapp
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

# Renders the index.html page with the result variable. If the request method is POST, it will run the pythonFunctions.findDurability function and return the result to the index.html page
@app.route('/raidtool', methods=['GET', 'POST']) 
def raidTool():
    if request.method == 'POST':
        input_data = request.form.get('getId')
        raidType = request.form.get('raidType')
        itemType = request.form.get('itemType')
        print(f"[CONSOLE] Itemtype: {itemType}, input: {input_data}, raidtype: {raidType}")
        result = pythonFunctions.findDurability(itemType, input_data, raidType)
        return render_template('raidtool.html', result=result)
    return render_template('raidtool.html', result="Waiting for input...")

@app.route('/recycletool', methods=['GET', 'POST'])
def recycleTool():
    if request.method == 'POST':
        input_item = request.form.get('getItem')
        result = list(pythonFunctions.findRecycleOutput(input_item))
        return render_template('recycletool.html', range = range(len(result)), result=result, item = f'Trying to recycle: {input_item}')
    return render_template('recycletool.html', result="Waiting for input...", range = range(0), item = "Waiting for input...")

@app.route('/')
def index():
    return render_template(use_template)

@app.route('/home')
def homePage():
    return render_template(use_template)

@app.route('/404')
def errorPage():
    return render_template('pageNotFound.html')

@app.route('/login')
def loginPage():
    return render_template('loginPage.html')

# Runs the app
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debugMode)