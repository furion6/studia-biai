from py3pin.Pinterest import Pinterest
from PIL import Image
import requests
from io import BytesIO


def download_image(url, path):
    r = requests.get(url=url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

pinterest = Pinterest(email='furionn6@gmail.com',
                      password='Madek1995',
                      username='furionn6',
                      cred_root='cred_root')



allpins = pinterest.search(scope='pins', query='something')
images = []
for pin in allpins:
	origUrl = pin['images']['orig']['url']
	images.append(origUrl)
		
i = 0
for url in images:
	#indx = str(url).rfind('.')
	#extension = str(url)[indx:]
	#download_image(url,  "img/" + str(i) + extension)
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))	
	img = img.resize((224,224))
	img.save("img/" + str(i)+".png", "PNG")
	i = i + 1


