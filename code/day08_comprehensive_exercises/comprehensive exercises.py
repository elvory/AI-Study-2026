students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72),
    ("David", 100),
    ("Eva", 85)
]

#按成绩从高到低排序
sorted_students = sorted(students, key = lambda student: student[1], reverse = True)
print(sorted_students)

#使用enumerate()函数获取学生的排名
enumerate_studnets = enumerate(sorted_students, start =1)
print(list(enumerate_studnets))

#找出成绩 >= 90 的学生姓名
students_names = [ name for name, score in students if score >= 90]
print(students_names)

students_dict = {name: score for name, score in students}
print(students_dict)
