"""
示例5：你的第一个完整 HTTP 请求
自己亲手打一遍！
"""

import requests

print("我的第一个 HTTP 请求")
print("-" * 30)

resp = requests.get("https://httpbin.org/get")

print("状态码：",resp.status_code)

data = resp.json()

print("你的IP：",data["origin"])
print("你的URL：",data["url"])

print("-" * 30)
print("✅ 完成！")