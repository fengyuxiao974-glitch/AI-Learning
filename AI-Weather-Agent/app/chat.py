"""
对话逻辑模块
支持 Function Calling
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
        self.tools = get_all_tools()  # 加载工具
        logger.info(f"✅ ChatBot 初始化成功 (模型: {self.model})")
        logger.info(f"🔧 已加载 {len(self.tools)} 个工具")

    def chat(self, messages):
        """
        对话 + Function Calling

        Args:
            messages: 对话历史

        Returns:
            str: AI 的回复
        """
        try:
            # 1. 调用 AI，附带工具定义
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools,  # ← 告诉 AI 有哪些工具可用
                tool_choice="auto",  # ← AI 自己决定是否调用工具
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )

            message = response.choices[0].message

            # 2. 检查 AI 是否想调用工具
            if message.tool_calls:
                logger.info(f"🔧 AI 想调用工具: {message.tool_calls[0].function.name}")

                # 3. 执行工具
                tool_call = message.tool_calls[0]
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                logger.info(f"📝 工具参数: {tool_args}")
                tool_result = execute_tool(tool_name, tool_args)
                logger.info(f"✅ 工具执行完成")

                # 4. 把 AI 的工具调用请求加入历史
                messages.append(message)

                # 5. 把工具执行结果加入历史
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result
                })

                # 6. 再次调用 AI，用工具结果生成最终回答
                second_response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens
                )

                return second_response.choices[0].message.content

                # 不需要调用工具，直接返回
            return message.content

        except Exception as e:
            error_msg = f"❌ AI 调用失败: {e}"
            logger.error(error_msg)
            return error_msg