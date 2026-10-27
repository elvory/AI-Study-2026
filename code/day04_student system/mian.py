print("Day04 Python File")


with open("learning.txt","w") as f:
    f.write("Python File Learning\n")
    f.write("AI Study 2026\n")


with open("learning.txt","r") as f:
    content = f.read()


print(content)



# Day04 小练习1：保存学生信息

students = [
    "凯凯,20,95\n",
    "小明,21,88\n",
    "小红,19,92\n"
]
#写入文件
with open("students.txt","w") as f:
    for student in students:
        f.write(student)

#读取文件
with open("students.txt","r") as f:
    content = f.read()

print("学生信息：\n" + content)



# Day04 小练习2：读取学生信息并分析


with open("students.txt", "r") as f:
    lines = f.readlines()


total_score = 0


print("学生列表:")


for line in lines:
    data = line.strip().split(",")

    name = data[0]
    age = data[1]
    score = int(data[2])

    total_score += score

    print(
        name,
        "年龄" + age,
        "成绩" + str(score)
    )


average = total_score / len(lines)


print()
print("平均成绩:", average)



# Day04 小练习3：成绩排行榜


students = []


with open("students.txt", "r") as f:
    lines = f.readlines()


for line in lines:

    data = line.strip().split(",")

    student = {
        "name": data[0],
        "age": int(data[1]),
        "score": int(data[2])
    }

    students.append(student)



# 排序
students.sort(
    key=lambda x: x["score"],
    reverse=True
)


print("成绩排行榜:")


for index, student in enumerate(students):

    print(
        index + 1,
        ".",
        student["name"],
        student["score"],
        "分"
    )

