"""
AI ChatBot v2.0 - 主程序入口
支持多轮对话、日志记录、配置管理
"""

import logging
from logging.handlers import RotatingFileHandler
import os
import sys

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import config
from app.chat import ChatBot


def setup_logging():
    """配置日志系统"""

    # 确保日志目录存在
    log_dir = os.path.dirname(config.LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 日志格式
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    # 配置根日志记录器
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format=log_format,
        datefmt=date_format,
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

    # 减少第三方库的日志输出
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    logger = logging.getLogger(__name__)
    logger.info(f"🚀 {config.APP_NAME} 启动")
    logger.info(f"📁 日志文件: {config.LOG_FILE}")


def main():
    """主程序"""

    # 1. 初始化日志
    setup_logging()
    logger = logging.getLogger(__name__)

    # 2. 打印欢迎信息
    print("=" * 50)
    print(f"   {config.APP_NAME}")
    print("=" * 50)
    print("命令: 输入消息对话")
    print("      'exit' 或 'quit' 退出")
    print("      'clear' 清空对话历史")
    print("      'status' 查看状态")
    print("=" * 50)

    # 3. 初始化 ChatBot
    try:
        bot = ChatBot()
    except ValueError as e:
        print(f"\n{e}")
        return

    # 4. 初始化对话历史
    messages = [
        {"role": "system", "content": config.SYSTEM_PROMPT}
    ]

    logger.info(f"📝 系统提示词: {config.SYSTEM_PROMPT[:50]}...")

    # 5. 对话循环
    while True:
        try:
            user_input = input("\n👤 你: ").strip()

            # 退出
            if user_input.lower() in ['exit', 'quit']:
                print("👋 再见！")
                logger.info("用户退出程序")
                break

            # 清空对话
            if user_input.lower() == 'clear':
                messages = [
                    {"role": "system", "content": config.SYSTEM_PROMPT}
                ]
                print("✅ 对话已清空")
                logger.info("对话历史已清空")
                continue

            # 查看状态
            if user_input.lower() == 'status':
                print(f"📊 对话轮数: {len(messages) // 2}")
                print(f"📊 消息总数: {len(messages)}")
                continue

            # 跳过空输入
            if not user_input:
                continue

            # 添加用户消息
            messages.append({"role": "user", "content": user_input})
            logger.info(f"👤 用户: {user_input[:50]}...")

            # 调用 AI
            print("🤔 AI 思考中...")
            reply = bot.chat(messages)

            # 添加 AI 回复到历史
            messages.append({"role": "assistant", "content": reply})

            # 显示回复
            print(f"\n🤖 AI: {reply}")

            # 显示对话轮数
            print(f"📊 对话轮数: {len(messages) // 2}")

        except KeyboardInterrupt:
            print("\n👋 再见！")
            logger.info("用户强制退出 (Ctrl+C)")
            break
        except Exception as e:
            logger.error(f"程序异常: {e}")
            print(f"❌ 发生错误: {e}")


if __name__ == "__main__":
    main()