"""
Day04 - HTTP + JSON + Requests
天气封装类
"""

import requests
import json
import os


class WeatherAPI:
    """天气API封装类"""

    def __init__(self,api_key=None):
        """
        初始化天气API客户端

        Args:
            api_key: API密钥，如果不穿则从环境变量读取
        """
        self.api_key = api_key or os.getenv("WEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5"

        if not self.api_key:
            print("警告：未设置WEATHER_API_KEY环境变量")
            print("  请创建 .env文件并添加: WEATHER_API_KEY=你的API密钥")

    def get_weather(self,city,units="metric"):
        """
        获取指定城市的当前空气
        Args:
            city:城市名（支持中文拼音，如Beijing,Shanghai）
            units:单位（metric=摄氏度，imperial=华氏度）

        Returns:
            dict: 天气信息或信息错误
        """
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "units": units,
            "appid": self.api_key,
            "lang": "zh-cn"
        }

        try:
            print(f"正在获取{city}的天气数据...")
            response = requests.get(url=url,params=params,timeout=10)

            if response.status_code == 200:
                data = response.json()
                return self._parse_weather_data(data)
            elif response.status_code == 401:
                return {"error": "❌ API Key 无效，请检查 .env 配置"}

            elif response.status_code == 404:
                return {"error": f"❌ 未找到城市: {city}"}

            else:
                return {"error": f"❌ 请求失败，状态码: {response.status_code}"}

        except requests.exceptions.Timeout:
            return {"error": "❌ 请求超时，请检查网络连接"}

        except requests.exceptions.ConnectionError:
            return {"error": "❌ 网络连接失败"}

        except json.JSONDecodeError:
            return {"error": "❌ 响应数据格式错误"}

        except Exception as e:
            return {"error": f"❌ 未知错误: {e}"}

    def _parse_weather_data(self, data):
        """
        解析天气数据，提取关键信息
        """
        weather_info = data.get("weather", [{}])[0]

        return {
            "city": data.get("name", "未知"),
            "country": data.get("sys", {}).get("country", "未知"),
            "temperature": data.get("main", {}).get("temp", 0),
            "feels_like": data.get("main", {}).get("feels_like", 0),
            "temp_min": data.get("main", {}).get("temp_min", 0),
            "temp_max": data.get("main", {}).get("temp_max", 0),
            "humidity": data.get("main", {}).get("humidity", 0),
            "pressure": data.get("main", {}).get("pressure", 0),
            "description": weather_info.get("description", "未知"),
            "icon": weather_info.get("icon", ""),
            "wind_speed": data.get("wind", {}).get("speed", 0),
            "clouds": data.get("clouds", {}).get("all", 0),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def display_weather(self, weather_data):
        """美观地显示天气信息"""
        if "error" in weather_data:
            print(f"\n{weather_data['error']}")
            return

        print("\n" + "=" * 50)
        print(f"  🌤️  {weather_data['city']}, {weather_data['country']}")
        print("=" * 50)
        print(f"  🌡️  温度: {weather_data['temperature']}°C")
        print(f"  🌡️  体感温度: {weather_data['feels_like']}°C")
        print(f"  🌡️  最低/最高: {weather_data['temp_min']}°C / {weather_data['temp_max']}°C")
        print(f"  ☁️  天气: {weather_data['description']}")
        print(f"  💧  湿度: {weather_data['humidity']}%")
        print(f"  📊  气压: {weather_data['pressure']} hPa")
        print(f"  💨  风速: {weather_data['wind_speed']} m/s")
        print(f"  ☁️  云量: {weather_data['clouds']}%")
        print(f"  🕐  更新时间: {weather_data['timestamp']}")
        print("=" * 50)


