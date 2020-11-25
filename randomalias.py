import requests
from PIL import Image
import os
import io
import json

session = requests.Session()
session.headers.update({'User-Agent': 'RandomAlias.py'})
face = session.get('https://thispersondoesnotexist.com/image')
info = session.get('https://randomuser.me/api/?nat=us')
baseinfoJSON = json.loads(info.text)
name = baseinfoJSON['results'][0]['name']['first'] + ' ' + baseinfoJSON['results'][0]['name']['last']
location = baseinfoJSON['results'][0]['location']
city = location['city']
state = location['state']
country = location['country']
zip = location['postcode']
 
f = io.BytesIO(face.content)
I = Image.open(f)
I.show()
print(name + '\n')
print(str(location['street']['number']) + ' ' + location['street']['name'] + ', ' + city + ', ' + state + ', ' + country + ', ' + str(zip))

