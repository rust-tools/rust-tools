import cgi
import json 
import test

form = cgi.FieldStorage()

input_data = form.getvalue('data')


result = test.findDurability("rustlabsDurabilityData.json", "deployable", input_data, "explo")

print("Content-Type: application/json\n")
print(json.dumps({'result': result}))