# Day04 小练习4 学生成绩管理系统


def load_students():

    students = []

    with open("students.txt","r") as f:

        lines = f.readlines()


    for line in lines:

        data = line.strip().split(",")

        student = {
            "name": data[0],
            "age": int(data[1]),
            "score": int(data[2])
        }

        students.append(student)


    return students



def show_students(students):

    print("\n学生列表:")

    for student in students:

        print(
            student["name"],
            "年龄:",
            student["age"],
            "成绩:",
            student["score"]
        )



def average_score(students):

    total = 0

    for student in students:

        total += student["score"]


    return total / len(students)


def rank_students(students):

    students.sort(
        key=lambda x:x["score"],
        reverse=True
    )


    print("\n成绩排行榜:")


    for i,student in enumerate(students):

        print(
            i+1,
            student["name"],
            student["score"],
            "分"
        )



students = load_students()


while True:


    print("""

1. 查看学生
2. 平均成绩
3. 退出

    """)


    choice = input("请选择:")



    if choice == "1":

        show_students(students)


    elif choice == "2":

        print(
            "平均成绩:",
            average_score(students)
        )


    elif choice == "3":

        print("退出系统")

        break


    else:

        print("输入错误")


