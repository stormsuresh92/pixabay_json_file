import requests
import json

f = open('pixabay.json',)

data = json.load(f)

for i in data['page']['results']:
    
   img_id = i['alt'].replace(',', '_').replace(' ', '_').replace('-', '_')
   
   img_url = i['sources']['2x']
   
   with open(img_id + '.jpg', 'wb') as f:
       
       links = requests.get(img_url)
       
       f.write(links.content)