import requests
import json

url = "https://api.languagetool.org/v2/check"

data = {
    'text': "Bonjou je suis un home!",
    'language': 'fr'
}

reponse = requests.post(url,data=data)
result = json.loads(reponse.text)
print(result)
