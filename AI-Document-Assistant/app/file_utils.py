"""
文件处理工具模块
支持读取 txt、json、csv 文件
"""

import os
import json
import csv
import logging

logger = logging.getLogger(__name__)


def read_text_file(file_path: str) -> str:
    """
    读取文本文件

    Args:
        file_path: 文件路径

    Returns:
        str: 文件内容
    """
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            content = f.read()
        logger.info(f"✅ 读取文本文件: {file_path} ({len(content)} 字符)")
        return content
    except FileNotFoundError:
        return f"❌ 文件不存在: {file_path}"
    except Exception as e:
        return f"❌ 读取失败: {e}"

def read_json_file(file_path: str) -> str:
    """
    读取 JSON 文件并格式化为文本

    Args:
        file_path: 文件路径

    Returns:
        str: 格式化的内容
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 格式化为可读文本
        formatted = json.dumps(data, ensure_ascii=False, indent=2)
        logger.info(f"✅ 读取 JSON 文件: {file_path}")
        return f"JSON 数据:\n{formatted}"

    except FileNotFoundError:
        return f"❌ 文件不存在: {file_path}"
    except json.JSONDecodeError as e:
        return f"❌ JSON 格式错误: {e}"
    except Exception as e:
        return f"❌ 读取失败: {e}"


def read_csv_file(file_path: str) -> str:
    """
    读取 CSV 文件并格式化为文本

    Args:
        file_path: 文件路径

    Returns:
        str: 格式化的内容
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)

        if not rows:
            return "❌ CSV 文件为空"

        # 格式化为文本表格
        headers = rows[0]
        data_rows = rows[1:]

        result = f"CSV 数据 (共 {len(data_rows)} 行):\n\n"
        result += " | ".join(headers) + "\n"
        result += "-" * 50 + "\n"

        for row in data_rows[:20]:  # 最多显示20行
            # 补齐列数
            while len(row) < len(headers):
                row.append("")
            result += " | ".join(row) + "\n"

        if len(data_rows) > 20:
            result += f"\n... 还有 {len(data_rows) - 20} 行"

        logger.info(f"✅ 读取 CSV 文件: {file_path} ({len(data_rows)} 行)")
        return result

    except FileNotFoundError:
        return f"❌ 文件不存在: {file_path}"
    except Exception as e:
        return f"❌ 读取失败: {e}"


def detect_file_type(file_path: str) -> str:
    """
    检测文件类型

    Args:
        file_path: 文件路径

    Returns:
        str: 文件扩展名 (txt, json, csv, md)
    """
    ext = os.path.splitext(file_path)[1].lower()
    return ext[1:] if ext else "unknown"


def read_file(file_path: str) -> str:
    """
    自动检测并读取文件

    Args:
        file_path: 文件路径

    Returns:
        str: 文件内容
    """
    file_type = detect_file_type(file_path)

    if file_type == "txt" or file_type == "md":
        return read_text_file(file_path)
    elif file_type == "json":
        return read_json_file(file_path)
    elif file_type == "csv":
        return read_csv_file(file_path)
    else:
        return f"❌ 不支持的文件类型: {file_type}"


def save_result(content: str, filename: str = "result.txt") -> str:
    """
    保存结果到文件

    Args:
        content: 要保存的内容
        filename: 文件名

    Returns:
        str: 保存结果信息
    """
    from .config import config

    try:
        # 确保输出目录存在
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)

        file_path = os.path.join(config.OUTPUT_DIR, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"✅ 保存结果: {file_path}")
        return f"✅ 结果已保存到: {file_path}"

    except Exception as e:
        return f"❌ 保存失败: {e}"


def list_files(directory: str = None) -> str:
    """
    列出目录中的文件

    Args:
        directory: 目录路径

    Returns:
        str: 文件列表
    """
    from .config import config

    target_dir = directory or config.DATA_DIR

    try:
        if not os.path.exists(target_dir):
            return f"❌ 目录不存在: {target_dir}"

        files = os.listdir(target_dir)
        if not files:
            return f"📁 {target_dir} 目录为空"

        result = f"📁 {target_dir} 中的文件:\n"
        for f in files:
            file_path = os.path.join(target_dir, f)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                result += f"  📄 {f} ({size} bytes)\n"
            else:
                result += f"  📁 {f}/\n"

        return result

    except Exception as e:
        return f"❌ 列出文件失败: {e}"

