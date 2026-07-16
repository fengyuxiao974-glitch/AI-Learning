"""
对话逻辑模块
封装 AI 调用逻辑
"""

import logging
from openai import OpenAI

from .config import config

# 获取日志记录器
logger = logging.getLogger(__name__)


class ChatBot:
    """AI 聊天机器人"""

    def __init__(self):
        """初始化客户端"""
        # 验证配置
        config.validate()

        self.client = OpenAI(
            api_key=config.DEEPSEEK_API_KEY,
            base_url=config.DEEPSEEK_BASE_URL
        )

        self.model = config.MODEL_NAME
        self.temperature = config.TEMPERATURE
        self.max_tokens = config.MAX_TOKENS

        logger.info(f"✅ ChatBot 初始化成功 (模型: {self.model})")

    def chat(self, messages):  # ← 参数名是 messages
        """
        调用 AI 进行对话

        Args:
            messages: 对话历史列表

        Returns:
            str: AI 的回复内容
        """
        try:
            # 调试：打印消息数量
            logger.debug(f"发送消息数: {len(messages)}")
            logger.debug(f"最后一条消息: {messages[-1]['content'][:50]}...")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,  # ← 这里用 messages
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )

            reply = response.choices[0].message.content
            logger.info(f"✅ AI 回复成功 (长度: {len(reply)} 字符)")

            return reply

        except Exception as e:
            error_msg = f"❌ AI 调用失败: {e}"
            logger.error(error_msg)
            return error_msg

    def reset(self):
        """重置客户端（用于切换模型等）"""
        logger.info("🔄 重置 ChatBot")
        self.__init__()