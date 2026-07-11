print("🤖 本地AI ChatBot已启动（输入 exit 退出）")

messages = []

while True:
    user_input = input("你：")

    if user_input.lower() == "exit":
        print("AI：再见！")
        break

    # 👉 记录用户输入（模拟 messages）
    messages.append({
        "role": "user",
        "content": user_input
    })

    # 🤖 模拟AI逻辑（规则版）
    if "你好" in user_input:
        ai_reply = "你好！我是你的本地AI助手。"
    elif "名字" in user_input:
        ai_reply = "我是一个模拟AI，用来帮助你学习ChatBot结构。"
    elif "你是谁" in user_input:
        ai_reply = "我是一个基于规则的AI模拟器。"
    else:
        ai_reply = f"你刚才说的是：{user_input}"

    print("AI：", ai_reply)

    # 👉 记录AI回复
    messages.append({
        "role": "assistant",
        "content": ai_reply
    })