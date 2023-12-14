import cgi
import json 
from test import findDurability ##FIXME: DOES NOT WORK

form = cgi.FieldStorage()

input_data = form.getvalue('data')


result = findDurability("rustlabsDurabilityData.json", "deployable", input_data, "explo")

print("Content-Type: application/json\n")
print(json.dumps({'result': result}))