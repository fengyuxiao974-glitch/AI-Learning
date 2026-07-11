"""
示例3：模拟 AI API 调用
理解 AI 对话的底层原理
"""

import json

print("=" * 50)
print("示例3：模拟 AI API 调用")
print("=" * 50)

# 这就是 AI API 请求的格式
request_data = {
    "model": "deepseek-chat",
    "messages":[
        {"role":"user","content":"你好，请介绍一下自己"}
    ],
    "temperature":0.7
}

print("📤 发送给 AI 的数据:")
print(json.dumps(request_data, ensure_ascii=False, indent=2))

# 模拟服务器返回
response_data = {
    "id": "chatcmpl-xxx",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "你好！我是 DeepSeek，一个 AI 助手。"
            }
        }
    ]
}

print("\n📥 AI 服务器返回:")
ai_message = response_data["choices"][0]["message"]["content"]
print(f"🤖 AI 回复: {ai_message}")
