from flask import Flask, render_template, session, request
import os
import python_functions
from app_settings import use_legacy, debug_mode

# Declare proper settings
if use_legacy:
    print("[CONSOLE] Using legacy UI")
    use_template = "index_legacy.html"
elif use_legacy == False:
    print("[CONSOLE] Using new UI")
    use_template = "index.html"

# Declares the app variable to start the webapp
app = Flask(__name__)


# Error handling, if page is not found, render 404 page.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pageNotFound.html', errorCode="404"), 404

# Renders the raidtool.html page with the result variable. If the request method is POST, it will run the pythonFunctions.findDurability function and return the result to the raidtool.html page
@app.route('/raidtool', methods=['GET', 'POST']) 
def raidTool():
    if request.method == 'POST':
        input_data = request.form.get('getId')
        raid_type = request.form.get('switch')
        print(raid_type)
        item_type = request.form.get('itemType')
        raid_tool = request.form.get('raidTool')
        if raid_type == 'on':
            raid_type = 'eco'
        elif raid_type == None:
            raid_type = 'explo'
        if raid_tool == 'None':
            raid_tool = None
        print(raid_type)
        print(f"[CONSOLE] Itemtype: {item_type}, input: {input_data}, raidtype: {raid_type}")
        result = python_functions.find_durability(item_type, 
                                                input_data, 
                                                raid_type,
                                                raid_tool)
        return render_template(
            'raidtool.html',
            result=result)
    return render_template(
        'raidtool.html', 
        result="Waiting for input...")

# Renders the recycletool.html page with the input_item variable. If the request method is POST, it will run the pythonFunctions.findRecycleOutput function and return the result to the recycletool.html page
@app.route(
        '/recycletool', 
        methods=['GET', 'POST'])
def recycleTool():
    if request.method == 'POST':
        input_item = request.form.get('getItem')
        result = list(python_functions.find_recycle_output(input_item))
        return render_template(
            'recycletool.html', 
            range = range(len(result)), 
            result=result, 
            item = f'Trying to recycle: {input_item}')
    return render_template(
        'recycletool.html', 
        result="Waiting for input...", 
        range = range(0), 
        item = "Waiting for input...")

# Renders the index.html page
@app.route('/')
def index():
    return render_template(use_template)

# Renders the home.html page
@app.route('/home')
def homePage():
    return render_template(use_template)

# Renders the pageNotFound.html page
@app.route('/404')
def errorPage():
    return render_template('pageNotFound.html')

# Renders the devPage.html page
@app.route('/in-development')
def devPage():
    return render_template('devPage.html')


# Runs the app
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)