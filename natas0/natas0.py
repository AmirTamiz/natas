import requests
exploit=requests.session()
exploit.auth=('natas0','natas0')
request=exploit.get('http://natas0.natas.labs.overthewire.org/')
#password has been in the source
print(request.text)