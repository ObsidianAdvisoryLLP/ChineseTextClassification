import requests
import json
from googletrans import Translator

translator = Translator()

response = requests.get(
    'https://datastudio-api.hkstp.org:443/scmparticlessample/v1.0/datastore_search?resource_id=0e27027d-ef86-4d03-ba99-3bb0fafec3f9', headers={'Authorization': 'Bearer bc891093a75ced9c19d3a8c030220c42'},verify = False)
response = json.loads(response.text)
translated_records = []

for record in response["result"]["records"]:
    record['translated'] = translator.translate(record["Title"] + record["Descriptions"], dest='zh-CN').text
    translated_records.append(record)
    with open('translated_records.json', 'w') as f:
        json.dump(translated_records, f, ensure_ascii=False)

with open('translated_records.json', 'w') as f:
        json.dump(translated_records, f, ensure_ascii=False)