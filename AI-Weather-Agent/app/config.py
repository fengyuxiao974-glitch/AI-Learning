"""
配置管理模块
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API 配置
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

    # 天气 API 配置
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "bd5e378503939ddaee76f12ad7a97608")

    # 模型配置
    MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-chat")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))

    # 日志配置
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

    @classmethod
    def validate(cls):
        if not cls.DEEPSEEK_API_KEY:
            raise ValueError("❌ DEEPSEEK_API_KEY 未设置！")
        return True

config = Config()