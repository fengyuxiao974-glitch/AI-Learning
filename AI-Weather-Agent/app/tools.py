"""
工具定义模块
定义 AI 可以调用的工具
"""

import json

# ============ 1. 定义工具 ============

# 天气查询工具的定义
GET_WEATHER_TOOL = {
    "type":"function",
    "function":{
        "name":"get_weather",
        "description":"获取指定城市的天气信息。当用户询问天气时调用此工具。",
        "parameters":{
            "type": "object",
            "properties":{
                "city":{
                    "type":"string",
                    "description":"城市名,如：北京、Shanghai、Hangzhou"
                },
                "units":{
                    "type":"string",
                    "enum":["metric","imperial"],
                    "description":"温度单位，metric=摄氏度，imperial=华氏度",
                    "default":"metric"
                }
            },
            "required":["city"]
        }
    }
}


# 计算器工具的定义
CALCULATE_TOOL = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "执行数学计算。当用户需要计算时调用此工具。",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "数学表达式，如：2 + 3, 10 * 5, 100 / 4"
                }
            },
            "required": ["expression"]
        }
    }
}# 计算器工具的定义
CALCULATE_TOOL = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "执行数学计算。当用户需要计算时调用此工具。",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "数学表达式，如：2 + 3, 10 * 5, 100 / 4"
                }
            },
            "required": ["expression"]
        }
    }
}


# ============ 2. 工具执行函数 ============

def execute_tool(tool_name: str, arguments: dict):
    """
    执行工具

    Args:
        tool_name: 工具名称
        arguments: 工具参数

    Returns:
        str: 工具执行结果
    """
    if tool_name == "get_weather":
        from .weather_api import get_weather, format_weather_info
        city = arguments.get("city", "")
        units = arguments.get("units", "metric")

        if not city:
            return "请提供城市名"

        weather_data = get_weather(city, units)
        return format_weather_info(weather_data)

    elif tool_name == "calculate":
        expression = arguments.get("expression", "")
        if not expression:
            return "请提供数学表达式"

        try:
            # 安全的计算
            result = eval(expression, {"__builtins__": {}})
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算错误: {e}"

    else:
        return f"未知工具: {tool_name}"

# ============ 3. 获取所有工具 ============

def get_all_tools():
    """获取所有工具的定义"""
    return [GET_WEATHER_TOOL, CALCULATE_TOOL]


def get_tool_by_name(name: str):
    """根据名称获取工具定义"""
    tools = get_all_tools()
    for tool in tools:
        if tool["function"]["name"] == name:
            return tool
    return None