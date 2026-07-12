"""
Day05 - 第一个AI ChatBot
基于DeepSeek API 实现多轮对话
"""

import os
from urllib import response

from dashscope.agentstudio import user_interrupt
from openai import OpenAI
from dotenv import load_dotenv

# ============ 1. 加载配置 ============
# 从 .env 文件读取 API Key
load_dotenv()

# 获取 API Key
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("❌ 错误：未找到 DEEPSEEK_API_KEY")
    print("请确保 .env 文件存在且包含正确的 API Key")
    exit(1)

# 初始化 AI 客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com" # DeepSeek API 地址
)

# ============ 2. 核心对话函数 ============
def chat_with_ai(messages):
    """
    调用AI进行对话

    参数：
        message:对话历史列表
        格式：[{"role":"user","content":"你好"},...]
    返回：
        AI的回复内容
    """
    try:
        #调用API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=2000
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ 出错了: {e}"

# ============ 3. 主程序 ============
def main():
    """多轮对话主程序"""

    print("=" * 50)
    print("   🤖 AI ChatBot v1.0")
    print("=" * 50)
    print("输入 'exit' 或 'quit' 退出")
    print("输入 'clear' 清空对话历史")
    print("=" * 50)

    # 初始化对话历史（包含系统提示词）
    messages = [
        {"role": "system", "content": "你是一位幽默的相声演员，用搞笑的方式回答。"}
    ]

    while True:
        #获取用户输入
        user_input = input("\n👤 你: ").strip()

        #退出
        if user_input.lower() in ["exit", "quit"]:
            print("👋 再见！")
            break

        # 清空对话
        if user_input.lower() == 'clear':
            messages = [
                {"role": "system", "content": "你是一位幽默的相声演员，用搞笑的方式回答。"}
            ]
            print("✅ 对话已清空")
            continue

        # 跳过空输入
        if not user_input:
            continue

        # 将用户消息加入历史
        messages.append({"role":"user","content":user_input})

        #调用AI
        print("🤔 AI 思考中...")
        reply = chat_with_ai(messages)

        #将AI回复加入历史
        messages.append({"role":"assistant","content":reply})

        #显示AI回复
        print(f"\n🤖 AI: {reply}")

        # 显示当前对话轮数
        print(f"📊 对话轮数: {len(messages) // 2}")

# ============ 4. 程序入口 ============
if __name__ == "__main__":
    main()