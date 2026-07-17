"""
对话逻辑模块
"""

import logging
from openai import OpenAI
from openai.types.responses import responses_client_event

from .config import config

logger = logging.getLogger(__name__)

class ChatBot:
    def __init__(self):
        config.validate()
        self.client = OpenAI(
            api_key=config.DEEPSEEK_API_KEY,
            base_url=config.DEEPSEEK_BASE_URL
        )
        self.model = config.MODEL_NAME
        self.temperature = config.TEMPERATURE
        self.max_tokens = config.MAX_TOKENS
        logger.info(f"✅ ChatBot 初始化成功")

    def chat(self,messages):
        try:
            responses = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return responses.choices[0].message.content
        except Exception as e:
            error_msg = f"❌ AI 调用失败: {e}"
            logger.error(error_msg)
            return error_msg
