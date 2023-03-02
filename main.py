import json

import requests

status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

base_url = 'https://petstore.swagger.io/v2'
post_url = '/pet'
headers_post = {'accept': 'application/json', 'Content-Type': 'application/json'}
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "cata"
  },
  "name": "Cat",
  "photoUrls": [
    "cat_foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "cat"
    }
  ],
  "status": "available"
}
data_post = json.dumps(new_pet)

r = requests.post(base_url + post_url, headers=headers_post, data=data_post)
try:
    result = r.json()
    id_new_pet = result.get('id')
except:
    result = r.text
    id_new_pet = int(result.split(':')[1].split(',')[0])
finally:
    print(result)


base_url = 'https://petstore.swagger.io/v2'
post_url = '/pet'
headers_post = {'accept': 'application/json', 'Content-Type': 'application/json'}
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "catan"
  },
  "name": "Cat",
  "photoUrls": [
    "cat_foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "cat"
    }
  ],
  "status": "available"
}
data_post = json.dumps(new_pet)

r = requests.put(base_url + post_url, headers=headers_post, data=data_post)
try:
    result = r.json()
    id_new_pet = result.get('id')
except:
    result = r.text
    id_new_pet = int(result.split(':')[1].split(',')[0])
finally:
    print(result)

r = requests.delete('https://petstore.swagger.io/v2/pet/9223372036854589580')
print(r.status_code)
print(res.text)

