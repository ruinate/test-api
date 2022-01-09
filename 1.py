import requests
from jsonpath_rw import jsonpath

url="https://bgapi.hzhuishi.cn/api/login"

data = {
    "username":"系统管理员",
    "password":"123456"
}

s=requests.post(url,data=data)

print(s.json())





