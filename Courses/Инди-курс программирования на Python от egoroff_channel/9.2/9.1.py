
import json
from pprint import pprint
from random import randint

dic_vk = """
{
    "response": {
        "count": 5945528,
        "items": [{
            "first_name": "Эммануил",
            "id": 504888197,
            "last_name": "Бердников",
            "can_access_closed": false
        }, {
            "first_name": "Надежда",
            "id": 558743443,
            "last_name": "Калинина",
            "can_access_closed": true
        }, {
            "first_name": "Ева",
            "id": 264805611,
            "last_name": "Півко",
            "can_access_closed": true
        }]
    }
}
"""


data = json.loads(dic_vk)
# pprint(data['response']['items'])

for item in data['response']['items']:
    del item['can_access_closed']
    del item['id']
    item['like'] = randint(1, 50000)

pprint(data['response']['items'])




with open('file.json', 'w') as f:
    json.dump(data, f, indent=3)