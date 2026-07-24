"""
对话逻辑模块 - 支持文件处理
"""

import logging
import json
from openai import OpenAI

from .config import config
from .tools import get_all_tools, execute_tool

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
        self.tools = get_all_tools()
        logger.info(f"✅ ChatBot 初始化成功")
        logger.info(f"🔧 已加载 {len(self.tools)} 个工具")

    def chat(self, messages):
        """
        对话 + Function Calling
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools,
                tool_choice="auto",
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )

            message = response.choices[0].message

            # 检查是否要调用工具
            if message.tool_calls:
                logger.info(f"🔧 AI 想调用工具: {message.tool_calls[0].function.name}")

                tool_call = message.tool_calls[0]
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                logger.info(f"📝 工具参数: {tool_args}")
                tool_result = execute_tool(tool_name, tool_args)
                logger.info(f"✅ 工具执行完成")

                # 把工具调用加入历史
                messages.append(message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result
                })

                # 再次调用 AI 生成最终回答
                second_response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens
                )

                return second_response.choices[0].message.content

            return message.content

        except Exception as e:
            error_msg = f"❌ AI 调用失败: {e}"
            logger.error(error_msg)
            return error_msg