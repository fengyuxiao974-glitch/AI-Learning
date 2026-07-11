"""
学生类 - 封装学生信息
"""

class Student:
    """学生类"""

    # 类变量（所有实例共享）
    school = "AI编程学校"

    def __init__(self,name,age,student_id):
        """构造函数：创建学生对象"""
        self.name = name
        self.age = age
        self.student_id = student_id
        self._grade = 0 # 受保护属性

    def set_grade(self,grade):
        """设置成疾（待验证）"""
        if 0 <= grade <= 100:
            self._grade = grade
            return True
        else:
            print("×成绩必须在0-100之间")
            return False

    def get_grade(self):
        """获取成绩"""
        return self._grade

    def study(self,hours):
        """学习，提高成绩"""
        if hours > 0:
            self._grade = min(100,self._grade + hours * 2)
            print(f"{self.name}学习了{hours}小时，成绩：{self._grade}")
        else:
            print("学习实践必须大于0")

    def display(self):
        """显示学生信息"""
        print(f"{self.student_id}|{self.name}|{self.age}岁|成绩：{self._grade}")

    def __str__(self):
        return f"学生({self.name},{self.age}岁，学号：{self._grade},成绩：{self._grade})"