"""
Day 1: Python 环境+基础语法
"""

print("=" * 50)
print("Day 1:Python 基础语法")
print("=" *50)

# 1. 变量
name = "AI Student"
age = 18
score = 95.5
is_learning = True

print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"分数{score}")
print(f"正在学习：{is_learning}")

# 2. 数据类型
print("\n数据类型")
print(f"name的类型：{type(name)}")
print(f"age的类型：{type(age)}")
print(f"score的类型：{type(score)}")
print(f"is_learning 的类型：{type(is_learning)}")

# 3. 输入输出
user_name = input("\n请输入你的名字")
print(f"你好，{user_name}!欢迎学习AI！")

# 4. 运算符
a,b = 10,3
print(f"\n运算:{a}+{b}={a+b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b}")
print(f"{a} // {b} = {a // b} (整除)")
print(f"{a} % {b} = {a % b} (余数)")
print(f"{a} ** {b} = {a ** b} (幂)")

# 5. 比较和逻辑运算
print(f"\n{a} > {b}: {a > b}")
print(f"{a} == {b}: {a == b}")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")