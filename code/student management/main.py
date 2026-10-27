#创建父类Student
class Student:
        def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.score = score

        def show_info(self):
            print(f"学生: {self.name}, 年龄: {self.age}, 成绩: {self.score}")

#创建子类GraduateStudent
class GraduateStudent(Student):
        def __init__(self, name, age, score, thesis_title):
            super().__init__(name, age, score)
            self.thesis_title = thesis_title

        #重写show_info方法以显示论文信息
        def show_info(self):
            super().show_info()
            print(f"论文: {self.thesis_title}")


#创建学生列表
students = [
    Student("张三", 20, 85),
    Student("王五", 22, 92),
    GraduateStudent("李四", 25, 90, "人工智能在医疗中的应用"),
    GraduateStudent("赵六", 26, 88, "机器学习在金融领域的应用")
]

print("  ===== 学生管理系统 =====  ")
for student in students:
    student.show_info()

#定义统计函数
def count_students(students):
    students_count = 0
    GraduateStudent_count = 0
    for student in students:
        if isinstance(student, GraduateStudent):
            GraduateStudent_count+=1
        elif isinstance(student, Student):
            students_count+=1
    return students_count, GraduateStudent_count

students_count, GraduateStudent_count = count_students(students)
print(f"普通学生数量:{students_count}")
print(f"研究生数量:{GraduateStudent_count}")



#成绩查询功能
def find_student(students, name):
    for student in students:
        if student.name == name:
            student.show_info()
            return
    print(f"未找到学生: {name}")

#测试查询功能
find_student(students, "Alice")


try:
     score = int(input("请输入成绩: "))
except ValueError:
     print("请输入有效的数字")
