import json
import requests

diag_url = "https://api.infermedica.com/v2/diagnosis"
cond_url = "https://api.infermedica.com/v2/conditions"
symp_url = "https://api.infermedica.com/v2/symptoms"

headers = {"Content-Type": "application/json", "App-Id": "26f8cff9", "App-Key": "54fe118921bd7051a284ae63e459b3df", "Dev-Mode": "true"}

#d_json = requests.post(diag_url, headers = headers).json()
c_json = requests.get(cond_url, headers = headers).json()
s_json = requests.get(symp_url, headers = headers).json()

with open('symptoms.json', 'w') as outfile:
    json.dump(s_json, outfile, indent=2)
with open('conditions.json', 'w') as outfile:
    json.dump(c_json, outfile, indent=2)


