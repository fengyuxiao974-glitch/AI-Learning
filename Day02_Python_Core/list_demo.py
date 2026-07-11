"""
Day 2:Python 核心用法 - 列表操作
"""

print("="*50)
print("列表操作")
print("="*50)

#1. 创建列表
fruits = ["苹果","香蕉","橙子"]
numbers = [1,2,3,4,5]
mixed = ["你好", 100,True,3.14]

print(f"水果列表：{fruits}")
print(f"数据列表{numbers}")
print(f"混合列表：{mixed}")

#2.访问元素（索引从0开始）
print(f"\n第一个水果：{fruits[0]}")
print(f"最后一个水果：{fruits[-1]}")
print(f"前两个水果：{fruits[0:2]}")

#3. 修改列表
fruits.append("西瓜")
print(f"\n添加西瓜后{fruits}")
fruits.insert(1,"草莓")
print(f"插入草莓后：{fruits}")
fruits.remove("香蕉")
print(f"删除香蕉后：{fruits}")
popped =  fruits.pop()
print(f"弹出：{popped}")
print(f"剩余：{fruits}")

#4. 列表遍历
print("\n遍历水果：")
for fruit in fruits:
    print(f" - {fruit}")

#5. 常规操作
print(f"\n列表长度：{len(fruits)}")
print(f"苹果在列表中？{'苹果'} in fruits")
print(f"排序：{sorted(fruits)}")
print(f"最大数：{max(numbers)}")
print(f"最小数{min(numbers)}")
print(f"求和：{sum(numbers)}")