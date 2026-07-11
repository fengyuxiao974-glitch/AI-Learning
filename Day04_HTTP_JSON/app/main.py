"""
Day04 - HTTP + JSON + Requests
"""

import os
import requests
from dotenv import load_dotenv
from app.api import WeatherAPI

#加载 .env 文件中的环境变量
load_dotenv()


def main():
    """主程序"""

    weather_api = WeatherAPI()

    print("=" * 50)
    print("   🌤️  天气查询工具 v1.0")
    print("=" * 50)
    print("命令说明:")
    print("  输入城市名    - 查询当前天气")
    print("  help          - 显示帮助")
    print("  quit          - 退出程序")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n🏙️  请输入城市名: ").strip()

            if user_input.lower() in ['quit','q','exit']:
                print("👋 再见！")
                break

            if user_input.lower() == ['help']:
                print("\n使用说明:")
                print("  输入城市拼音查询天气，如: Beijing, Shanghai, Hangzhou")
                continue

            if not user_input:
                continue

            weather_data = weather_api.get_weather(user_input)
            weather_api.display_weather(weather_data)

            if "error" not in weather_data:
                print("\n📄 原始JSON响应 (前200字符):")
                print(json.dumps(weather_data, ensure_ascii=False, indent=2)[:200] + "...")

        except KeyboardInterrupt:
            print(print("\n👋 再见！"))
            break
        except Exception as e:
            print(f"❌ 程序错误: {e}")


if __name__ == "__main__":
    main()




