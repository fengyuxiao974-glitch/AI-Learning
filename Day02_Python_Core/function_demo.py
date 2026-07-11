"""
Day Python 核心语法 - 函数
"""

# 1. 定义函数
def greet(name):
    """打招呼函数"""
    return f"你好，{name}！"

print(greet("小明"))

# 2. 参数类型
def add(a,b):
    """两数相加"""
    return a+b

def greet_with_title(name, title="同学"):
    """带默认参数"""
    return f"{title}{name}"

print(f"\nadd(3,5) = {add(3,5)}")
print(greet_with_title("小明"))
print(greet_with_title("小明","老师"))

# 3. 不定长参数
def sum_all(*args):
    """任何数量关键词参数"""
    return sum(args)

def print_info(**kwargs):
    """任意数量关键字参数"""
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print(f"\nsum_all(1,2,3,4) = {sum_all(1,2,3,4)}")
print("\nprint_info:")
print_info(name="小明", age=25, city="杭州")

# 4. 返回值
def get_user_info():
    """返回多个值"""
    return "小明", 25,"杭州"

name,age,city =get_user_info()
print(f"\n返回多个值：{name}，{age}，{city}")

# 5. lambda 函数
square = lambda x: x ** 2
print(f"\nlambda平方：{square(5)}")

# 6. 练习：数据处理
def process_data(data,operation):
    """
    处理数据：支持sum,avg,max,min

    Args:
        data:数据类型
        operation:操作类型

    Returns:
        处理结果
    """
    if not data:
        return None

    if operation == "sum":
        return sum(data)
    elif operation == "avg":
        return sum(data) / len(data)
    elif operation == "max":
        return max(data)
    elif operation == "min":
        return min(data)
    else:
        return "不支持操作"

# 测试
scores = [85,92,78,90,88]
print(f"\n成绩：{scores}")
print(f"总和：{process_data(scores,'sum')}")
print(f"平均分：{process_data(scores,'avg')}")
print(f"最高分：{process_data(scores,'max')}")
print(f"最低分：{process_data(scores,'min')}")