'''
import base64
encode = base64.b64encode(b'Nzg0ODYyOTkxODI4Nzc5MDk5.X8venw.0NCy2ayWKGJhsoVVOvx4HTEbGOc')
decrypt = base64.b64decode(encode)
print(encode)
print(decrypt)
'''
'''
https://stackoverflow.com/questions/62338957/downloading-random-images-from-google-using-python
import os
import sys
import urllib
import urllib2
import json
import random
import imghdr

if len(sys.argv) <= 1:
  print('Usage:')
  print('python fetch_google_image.py cat cute')
  exit()

q = ''

for arg in sys.argv[1:]:
  q += urllib.quote(arg) + '+'

f = urllib2.urlopen('http://ajax.googleapis.com/ajax/services/search/images?q=' + q + '&v=1.0&rsz=large&start=1')
data = json.load(f)
f.close()

results = data['responseData']['results']
url = results[random.randint(0, len(results) - 1)]['url']
urllib.urlretrieve(url, './image')

imagetype = imghdr.what('./image')
if not(type(imagetype) is None):
  os.rename('./image', './image.' + imagetype)
'''

help = """
___COMMANDS___

--spam 		(--spam <message> <Time>)
--AI   		(--AI <message>)
--image 	(--image <message>)
--help (print out this help command manual) 


___EXAMPLE SYNTAX___

!sp <mode> <option>


___SPECIFIC HELP___

!sp help <mode>
Ex: !sp help spam

 """

with open("Menu.txt", "a") as file:
    file.write(help)