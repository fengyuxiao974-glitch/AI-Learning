"""
示例4：实战 - 调用真实天气 API
"""

import requests
import json

print("=" * 50)
print("示例4：调用真实天气 API")
print("=" * 50)

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
CITY = "Hangzhou"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric",
    "lang": "zh_cn"
}

print(f"\n请求 URL: {url}")
print(f"参数: {params}")

try:
    response = requests.get(url, params=params, timeout=10)

    print(f"\n状态码: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"\n🌤️ 城市: {data['name']}")
        print(f"🌡️ 温度: {data['main']['temp']}°C")
        print(f"💧 湿度: {data['main']['humidity']}%")
        print(f"☁️ 天气: {data['weather'][0]['description']}")
    else:
        print(f"❌ 请求失败: {response.status_code}")

except Exception as e:
    print(f"❌ 错误: {e}")