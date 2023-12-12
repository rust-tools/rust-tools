import cgi
import json 
import findDurability

form = cgi.FieldStorage()

input_data = form.getvalue('data')


result = rldb.findDurability("rustlabsDurabilityData.json", "deployable", input_data, "explo")

print("Content-Type: application/json\n")
print(json.dumps({'result': result}))