"""
Day 2: Python 核心用法 - 字典和集合
"""

print("="*50)
print("字典和集合")
print("="*50)

# 1. 创建字典
person = {
    "name": "小明",
    "age": 25,
    "city":"杭州",
    "hobbies": ["读书","跑步"]
}

print(f"个人信息：{person}")

# 2. 访问字典
print(f"\n姓名：{person['name']}")
print(f"年龄：{person.get('age','未知')}")
print(f"不存在的键：{person.get('score','不存在')}")

# 3. 修改字典
person["age"] = 26
person["job"] = "工程师"
print(f"\n修改后：{person}")

# 4. 遍历字典
print("\n遍历字典：")
for key,value in person.items():
    print(f" {key}: {value}")

# 5. 字典推导式
squares_dict = {x: x**2 for x in range(1,6)}
print(f"\n数字-平方：{squares_dict}")

# 6. 集合（去重）
numbers = [1,2,2,3,3,3,4,4,4,4]
unique_numbers = set(numbers)
print(f"\n原始列表: {numbers}")
print(f"去重后：{unique_numbers}")

# 7. 集合运算
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(f"\n集合1：{set1}")
print(f"集合2：{set2}")
print(f"并集：{set1 | set2}")
print(f"交集：{set1 & set2}")
print(f"差集：{set1 - set2}")
