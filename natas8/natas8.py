import requests

url="http://natas8.natas.labs.overthewire.org/index.php"
exploit=requests.session()
data={'secret':'oubWYf2kBq','submit':'Submit Query'}
exploit.auth=('natas8','DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe')
request=exploit.post(url,data)
#password has been in the source
print(request.text)