"""
AI 天气助手 - 支持 Function Calling
"""

import logging
from logging.handlers import RotatingFileHandler
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import config
from app.chat import ChatBot


def setup_logging():
    log_dir = os.path.dirname(config.LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(
                config.LOG_FILE,
                maxBytes=10 * 1024 * 1024,
                backupCount=5,
                encoding='utf-8'
            )
        ]
    )

    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)


def print_menu():
    print("\n" + "=" * 60)
    print("   🌤️ AI 天气助手 (支持 Function Calling)")
    print("=" * 60)
    print("功能:")
    print("  📍 查询天气 - 输入城市名即可")
    print("  🧮 数学计算 - 如: 计算 2+3")
    print("  💬 普通对话 - 随便聊天")
    print("=" * 60)
    print("命令:")
    print("  /clear  - 清空对话")
    print("  /status - 查看状态")
    print("  /exit   - 退出")
    print("=" * 60)


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        bot = ChatBot()
    except ValueError as e:
        print(f"\n{e}")
        return

    messages = [
        {"role": "system", "content": "你是一个有用的AI助手，可以查询天气和执行计算。"}
    ]

    print_menu()
    logger.info("AI 天气助手启动")

    while True:
        try:
            user_input = input("\n👤 你: ").strip()

            if user_input.lower() in ['/exit', '/quit']:
                print("👋 再见！")
                break

            if user_input.lower() == '/clear':
                messages = [
                    {"role": "system", "content": "你是一个有用的AI助手，可以查询天气和执行计算。"}
                ]
                print("✅ 对话已清空")
                continue

            if user_input.lower() == '/status':
                print(f"📊 对话轮数: {len(messages) // 2}")
                continue

            if not user_input:
                continue

            messages.append({"role": "user", "content": user_input})

            print("🤔 AI 思考中...")
            reply = bot.chat(messages)

            messages.append({"role": "assistant", "content": reply})

            print(f"\n🤖 AI: {reply}")
            print(f"📊 对话轮数: {len(messages) // 2}")

        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            logger.error(f"程序异常: {e}")
            print(f"❌ 发生错误: {e}")


if __name__ == "__main__":
    main()