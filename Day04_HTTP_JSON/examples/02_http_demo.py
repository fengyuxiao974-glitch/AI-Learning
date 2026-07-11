"""
示例2：理解HTTP请求结构
"""

import requests

print("=" * 50)
print("示例2：带参数的 HTTP 请求")
print("=" * 50)

params = {
    "name":"Fengyuxiao",
    "age": 20,
    "city": "Hangzhou"
}

response = requests.get("http://httpbin.org/get", params=params)
data = response.json()

print(f"请求URL:{data['url']}")
print(f"\n服务器收到的参数:")
print(data['args'])