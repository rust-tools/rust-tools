from flask import Flask, render_template, request
import pythonFunctions

# Declares the app variable to start the webapp
app = Flask(__name__)

# Renders the index.html page with the result variable. If the request method is POST, it will run the pythonFunctions.findDurability function and return the result to the index.html page
@app.route('/', methods=['GET', 'POST']) 
def home():
    if request.method == 'POST':
        input_data = request.form.get('getId')
        raidType = request.form.get('raidType')
        itemType = request.form.get('itemType')
        print(itemType, input_data, raidType)
        result = pythonFunctions.findDurability(itemType, input_data, raidType)
        return render_template('index.html', result=result)
    return render_template('index.html', result="waiting for input")

# Runs the app
if __name__ == "__main__":
    app.run(debug=False)