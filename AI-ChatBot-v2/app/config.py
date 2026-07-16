"""
配置管理模块
统一管理所有配置项
"""

import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()


class Config:
    """配置类"""

    #API配置
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

    #模型配置
    MODEL_NAME = os.getenv("MODEL_NAME","deepseek-chat")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))

    #日志配置
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE","logs/app.log")

    #应用配置
    APP_NAME = os.getenv("APP_NAME","AI Chat v2.0")
    SYSTEM_PROMPT = os.getenv(
        "SYSTEM_PROMPT",
        "你是一个有用的AI助手，用中文回答。"
    )

    @classmethod
    def validate(cls):
        """验证必要配置是否存在"""
        if not cls.DEEPSEEK_API_KEY:
            raise ValueError(
                "❌ DEEPSEEK_API_KEY 未设置！\n"
                "请在 .env 文件中设置 DEEPSEEK_API_KEY=你的API密钥"
            )
        return True


config = Config()