import cgi
import json 
<<<<<<< HEAD
import findDurability
=======
import test
>>>>>>> origin

form = cgi.FieldStorage()

input_data = form.getvalue('data')


<<<<<<< HEAD
result = rldb.findDurability("rustlabsDurabilityData.json", "deployable", input_data, "explo")
=======
result = test.findDurability("rustlabsDurabilityData.json", "deployable", input_data, "explo")
>>>>>>> origin

print("Content-Type: application/json\n")
print(json.dumps({'result': result}))