import requests
import json
from datetime import datetime

response = requests.get("http://api.open-notify.org/astros.json")
pos = requests.get("http://api.open-notify.org/iss-now.json")
print("\nStatus code: ",response.status_code)

print("\n\nNo. of people on ISS currently: ", response.json()["number"],"\n\nTheir Names: ")

names = response.json()["people"]
for n in names:
	print(n["name"].rstrip())
	
#print(json.dumps(pos.json(), sort_keys=True, indent=4))
	
geo_params = {
	'LAT':pos.json()['iss_position']['latitude'],
	'LNG':pos.json()['iss_position']['longitude']
}

time = datetime.fromtimestamp(pos.json()['timestamp'])

rgeocode = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={geo_params['LAT']}+{geo_params['LNG']}&key=e4c20439815d4deda3eb510ab508704b")


print('\n\n',time)
print("Coordinates: ",geo_params['LAT'],geo_params['LNG'])

#print(json.dumps(rgeocode.json()['results'], sort_keys=True, indent=4))
print("Current location: ",rgeocode.json()['results'][0]['formatted'])
print("Three words locator: ",rgeocode.json()['results'][0]['annotations']["what3words"])
print("Confidence Level: ",rgeocode.json()['results'][0]["confidence"])

