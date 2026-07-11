"""
实例1： 第一个HTTP请求
"""
from urllib import response

import requests

print("=" * 50)
print("示例1：发送GET请求")
print("=" * 50)

resonse = requests.get("https://httpbing.org/get")

print(f"状态码：{response.status_code}")
print(f"\n相应内容（JSON）:")
data = response.json()
print(data)

print(f"\n你的IP地址：{data['origin']}")