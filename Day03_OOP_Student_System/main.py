"""
学生管理系统 - 主程序
"""

from student import Student

class StudentManager:
    """学生管理系统"""

    def __init__(self):
        self.students = []
        self.next_id = 1

    def add_student(self,name,age):
        """添加学生"""
        student = Student(name,age,f"S{self.next_id:04d}")
        self.students.append(student)
        self.next_id += 1
        print(f"添加成功：{student}")
        return student

    def find_by_id(self,student_id):
        """根据学号查找"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_by_name(self,name):
        """根据名字查找"""
        results = []
        for student in self.students:
            if name in student.name:
                results.append(student)
        return results

    def delete_student(self,student_id):
        """删除学生"""
        student = self.find_by_id(student_id)
        if student:
            self.students.remove(student)
            print(f"已删除：{student}")
            return True
        print(f"×未找到学号 {student_id}")
        return False

    def list_all(self):
        """列出所有学生"""
        if not self.students:
            print("暂无学生")
            return

        print("\n"+"="*50)
        print("学号\t姓名\t年龄\t成绩")
        print("-"*50)
        for student in self.students:
            print(f"{student.student_id}\t{student.name}\t{student.age}\t{student.get_grade()}")
        print("-"*50)


def main():
    """主程序"""
    manager = StudentManager()

    print("=" * 50)
    print("  学生管理系统")
    print("=" * 50)
    print("命令：add,find,delete,list,quit")
    print("=" * 50)

    while True:
        try:
            cmd = input("\n请输入命令：").strip().lower()

            if cmd in ['quit','q']:
                print("再见！")
                break

            elif cmd == 'add':
                name = input("姓名：")
                age = int(input("年龄："))
                manager.add_student(name,age)

            elif cmd == 'find':
                search = input("输入学号或姓名: ").strip()
                if not search:
                    print("❌ 请输入关键词")
                    continue

                # ===== 修改点开始 =====
                # 判断是学号还是姓名
                # 如果输入以 S 开头且长度 >= 2，当作学号查找
                if search.upper().startswith('S') and len(search) >= 2:
                    student = manager.find_by_id(search.upper())
                    if student:
                        print("\n找到学生:")
                        student.display()
                    else:
                        print(f"❌ 未找到学号 {search}")
                else:
                    # 否则按姓名查找（支持模糊匹配）
                    results = manager.find_by_name(search)
                    if results:
                        print(f"\n找到 {len(results)} 个匹配结果:")
                        for student in results:
                            student.display()
                    else:
                        print(f"❌ 未找到姓名包含 '{search}' 的学生")
                # ===== 修改点结束 =====

            elif cmd == 'delete':
                student_id = input("学号：")
                manager.delete_student(student_id)

            elif cmd == 'list':
                manager.list_all()

            else:
                print("未知命令：add,find,list,quit")

        except ValueError:
            print("请输入正确的数字")
        except Exception as e:
            print(f"错误：{e}")


if __name__ == "__main__":
    main()