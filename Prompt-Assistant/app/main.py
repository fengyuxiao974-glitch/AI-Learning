"""
Prompt Engineering 实战
学习如何设计高质量的 Prompt
"""

import logging
from idlelib.iomenu import encoding
from logging import currentframe
from logging.handlers import RotatingFileHandler
import os
import sys

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .config import config
from .chat import ChatBot
from .prompts import (
    get_system_prompt,
    list_styles,
    list_roles,
    EMOTION_FEW_SHOT,
    CODE_EXPLAIN_FEW_SHOT,
    SUMMARY_FEW_SHOT,
    COT_PROMPT
)


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
                maxBytes=10*1024*1024,
                backupCount=5,
                encoding='utf-8'
            )
        ]
    )

    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)


def print_menu():
    """打印功能菜单"""
    print("\n" + "=" * 60)
    print("   🎯 Prompt Engineering 助手")
    print("=" * 60)
    print("命令说明:")
    print("  直接输入消息    - 普通对话")
    print("  /style 风格名   - 切换助手风格 (如 /style coder)")
    print("  /role 角色名   - 切换角色扮演 (如 /role 李白)")
    print("  /fewshot       - 使用 Few-shot 示例")
    print("  /cot          - 使用 Chain of Thought")
    print("  /list         - 查看所有风格和角色")
    print("  /status       - 查看当前状态")
    print("  /clear        - 清空对话")
    print("  /exit         - 退出")
    print("=" * 60)

    print("\n📋 可用风格:")
    styles = list_styles()
    for i, style in enumerate(styles, 1):
        print(f"   {i}. {style}")

    print("\n📋 可用角色:")
    roles = list_roles()
    for i, role in enumerate(roles, 1):
        print(f"   {i}. {role}")

    print("\n💡 提示:")
    print("   /style 风格名  → 切换风格")
    print("   /role 角色名   → 切换角色")
    print("=" * 60)


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        bot = ChatBot()
    except ValueError as e:
        print(f"\n{e}")
        return

    current_style ="default"
    current_system_prompt = get_system_prompt(current_style)

    messages = [
        {"role":"system","content":current_system_prompt},
    ]

    print_menu()
    logger.info(f"启动 Prompt 助手，当前风格: {current_style}")

    while True:
        try:
            user_input = input("\n👤 你: ").strip()

            # === 命令处理 ===

            if user_input.lower() in ["/exit","/quit"]:
                print("👋 再见！")
                break

            if user_input.lower() == "/clear":
                messages = [
                    {"role":"system","content":current_system_prompt},
                ]
                print("✅ 对话已清空")
                continue

            if user_input.lower() == '/list':
                print("\n📋 可用风格:")
                for s in list_styles():
                    print(f"   {s}")
                print("\n📋 可用角色:")
                for r in list_roles():
                    print(f"   {r}")
                continue

            # === 切换风格 ===
            if user_input.startswith("/style "):
                style = user_input[7:].strip()
                if style in list_styles():
                    current_style = style
                    current_system_prompt = get_system_prompt(style)
                    messages = [
                    {"role":"system","content":current_system_prompt},
                    ]
                    print(f"✅ 已切换到风格: {style}")
                    logger.info(f"切换风格: {style}")
                else:
                    print(f"❌ 未找到风格: {style}")
                    print(f"   可用: {', '.join(list_styles())}")
                continue

            # === 切换角色 ===
            if user_input.startswith("/role "):
                role = user_input[6:].strip()
                from .prompts import get_role_prompt
                role_prompt = get_role_prompt(role)
                if role_prompt:
                    current_system_prompt = role_prompt
                    messages = [
                        {"role":"system","content":current_system_prompt},
                    ]
                    print(f"✅ 已切换到角色: {role}")
                    logger.info(f"切换角色: {role}")
                else:
                    print(f"❌ 未找到角色: {role}")
                    print(f"   可用: {', '.join(list_roles())}")
                continue

            # === Few-shot 示例 ===
            if user_input.lower() == '/fewshot':
                print("\n📝 选择 Few-shot 示例:")
                print("   1. 情感分类")
                print("   2. 代码解释")
                print("   3. 文本摘要")

                choice = input("请选择 (1-3): ").strip()

                if choice == "1":
                    messages.append({"role":"user","content": EMOTION_FEW_SHOT})
                elif choice == '2':
                    messages.append({"role":"user","content": CODE_EXPLAIN_FEW_SHOT})
                elif choice == '3':
                    messages.append({"role":"user","content": SUMMARY_FEW_SHOT})
                else:
                    print("❌ 无效选择")
                    continue

            # === Chain of Thought ===
            if user_input.lower() == '/cot':
                messages.append({"role":"user","content": COT_PROMPT})
                print("✅ 已加载 Chain of Thought 提示")
                print("💡 现在输入要分析的问题")
                continue

            # === 普通对话 ===
            if not user_input:
                continue

            messages.append({"role":"user","content":user_input})

            print("🤔 AI 思考中...")
            reply = bot.chat(messages)

            messages.append({"role":"system","content":reply})

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

