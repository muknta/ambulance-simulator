import json
import requests
#curl "https://api.infermedica.com/v2/diagnosis" \
#  -X "POST" \
#  -H "App-Id: 26f8cff9" -H "App-Key: 54fe118921bd7051a284ae63e459b3df" \
#  -H "Content-Type: application/json" \
#  -H "Dev-Mode: true" \
#  -d '{"sex":"male", "age":30, "evidence":[{"id":"c_275", "choice_id":"present"}]}'url = "https://priaid-symptom-checker-v1.p.rapidapi.com/specialisations?language=en-gb"
url = "https://api.infermedica.com/v2/diagnosis"
headers = {"Content-Type": "application/json", "App-Id": "26f8cff9", "App-Key": "54fe118921bd7051a284ae63e459b3df", "Dev-Mode": "true"}
data = {"sex": "female", "age": 25, "evidence": [{"id": "s_47", "choice_id": "present", "initial": "true"}, {"id": "s_22", "choice_id": "present", "initial": "true"}, {"id": "p_81", "choice_id": "absent"}], "extras": { "disable_groups": "true"}}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())


