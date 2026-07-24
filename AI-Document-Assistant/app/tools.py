"""
工具定义模块
定义文件处理工具
"""

# ============ 1. 工具定义 ============

READ_FILE_TOOL = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "读取文件内容。支持 txt、json、csv、md 格式。当用户提到文件时调用此工具。",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "文件路径，如 data/sample.txt"
                }
            },
            "required": ["file_path"]
        }
    }
}

LIST_FILES_TOOL = {
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "列出目录中的所有文件。当用户想查看有哪些文件时调用此工具。",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "目录路径，默认为 data 目录",
                    "default": "data"
                }
            }
        }
    }
}

SAVE_RESULT_TOOL = {
    "type": "function",
    "function": {
        "name": "save_result",
        "description": "保存处理结果到文件。当 AI 分析完文件后，保存结果。",
        "parameters": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "要保存的内容"
                },
                "filename": {
                    "type": "string",
                    "description": "保存的文件名，如 summary.txt",
                    "default": "result.txt"
                }
            },
            "required": ["content"]
        }
    }
}


# ============ 2. 工具执行函数 ============

def execute_tool(tool_name: str, arguments: dict) -> str:
    """
    执行工具

    Args:
        tool_name: 工具名称
        arguments: 工具参数

    Returns:
        str: 工具执行结果
    """
    from .file_utils import read_file, list_files, save_result

    if tool_name == "read_file":
        file_path = arguments.get("file_path", "")
        if not file_path:
            return "❌ 请提供文件路径"
        return read_file(file_path)

    elif tool_name == "list_files":
        directory = arguments.get("directory", "data")
        return list_files(directory)

    elif tool_name == "save_result":
        content = arguments.get("content", "")
        filename = arguments.get("filename", "result.txt")
        if not content:
            return "❌ 请提供要保存的内容"
        return save_result(content, filename)

    else:
        return f"❌ 未知工具: {tool_name}"


# ============ 3. 获取所有工具 ============

def get_all_tools():
    """获取所有工具的定义"""
    return [READ_FILE_TOOL, LIST_FILES_TOOL, SAVE_RESULT_TOOL]