"""
天气 API 调用模块
"""

import requests
import json
import logging

logger = logging.getLogger(__name__)


def get_weather(city: str, units: str = "metric") -> dict:
    """
    获取指定城市的天气

    Args:
        city: 城市名（中文或拼音）
        units: 单位 (metric=摄氏度, imperial=华氏度)

    Returns:
        dict: 天气信息
    """
    from .config import config

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": config.WEATHER_API_KEY,
        "units": units,
        "lang": "zh_cn"
    }

    try:
        logger.info(f"🌤️ 查询天气: {city}")
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            # 提取关键信息
            weather_info = {
                "city": data.get("name", city),
                "country": data.get("sys", {}).get("country", ""),
                "temperature": data.get("main", {}).get("temp", 0),
                "feels_like": data.get("main", {}).get("feels_like", 0),
                "humidity": data.get("main", {}).get("humidity", 0),
                "description": data.get("weather", [{}])[0].get("description", "未知"),
                "wind_speed": data.get("wind", {}).get("speed", 0),
                "temp_min": data.get("main", {}).get("temp_min", 0),
                "temp_max": data.get("main", {}).get("temp_max", 0),
            }

            logger.info(f"✅ 获取 {city} 天气成功")
            return weather_info

        elif response.status_code == 404:
            return {"error": f"未找到城市: {city}"}

        else:
            return {"error": f"请求失败: {response.status_code}"}

    except requests.exceptions.Timeout:
        return {"error": "请求超时"}
    except requests.exceptions.ConnectionError:
        return {"error": "网络连接失败"}
    except Exception as e:
        return {"error": f"未知错误: {e}"}


def format_weather_info(weather_data: dict) -> str:
    """
    格式化天气信息为自然语言

    Args:
        weather_data: get_weather 返回的数据

    Returns:
        str: 自然语言描述的天气
    """
    if "error" in weather_data:
        return f"❌ {weather_data['error']}"

    city = weather_data.get("city", "未知")
    temp = weather_data.get("temperature", 0)
    feels_like = weather_data.get("feels_like", 0)
    desc = weather_data.get("description", "未知")
    humidity = weather_data.get("humidity", 0)
    wind = weather_data.get("wind_speed", 0)
    temp_min = weather_data.get("temp_min", 0)
    temp_max = weather_data.get("temp_max", 0)

    return f"""
📊 {city} 天气报告：
  🌡️ 温度: {temp}°C (体感 {feels_like}°C)
  🌡️ 最低/最高: {temp_min}°C / {temp_max}°C
  ☁️ 天气: {desc}
  💧 湿度: {humidity}%
  💨 风速: {wind} m/s
"""