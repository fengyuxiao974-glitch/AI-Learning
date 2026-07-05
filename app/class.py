from ctypes import pythonapi


class Student:
    def __init__(self,name,age,major):
        self.name=name
        self.age=age
        self.major=major

    def introduce(self):
        print(f"姓名:{self.name}")
        print(f"年龄:{self.age}")
        print(f"专业:{self.major}")

    def study(self,subject):
        print(self.name+"正在学习"+subject)


me = Student("fengyuxiao", 20 ,"chemical engineer")

me.introduce()
me.study("python")