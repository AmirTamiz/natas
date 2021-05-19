import requests
exploit=requests.session()
exploit.auth=('natas1','gtVrDuiDfck831PqWsLEZy5gyDz1clto')
request=exploit.get('http://natas1.natas.labs.overthewire.org/')
#password has been in the source
print(request.text)