# Day03 Python基础练习
# 变量与数据类型


# 字符串 string
student_name = "AI Student"


# 整数 int
age = 20


# 浮点数 float
python_score = 95.5


# 布尔值 bool
learning_ai = True


# 列表 list
skills = [
    "Python",
    "Git",
    "AI"
]


# 字典 dict
student = {
    "name": student_name,
    "age": age,
    "score": python_score
}


print(student_name)
print(age)
print(python_score)
print(learning_ai)

print(skills)

print(student)



student_name="凯凯"
age=20
height=1.7
is_student=True


print(student_name)
print(age)
print(height)
print(is_student)


print(type(student_name))
print(type(age))
print(type(height))
print(type(is_student))



# 计算练习

name = "凯凯"

age = 20

next_age = age + 1


print(name)

print("明年年龄:", next_age)


# AI模型信息

model_name = "ChatGPT"

version = "GPT"

accuracy = 0.95


print(model_name)

print(version)

print(accuracy)


# Day03-2 List练习


skills = ["Python", "Git", "AI"]


print(skills)


print(skills[0])


skills.append("Machine Learning")


print(skills)


skills[1] = "GitHub"


print(skills)

# AI数据列表练习

models = [
    "CNN",
    "RNN",
    "Transformer"
]


print(models)

print("模型数量:", len(models))


models.append("GPT")


print(models)

print("最新模型:", models[3])



# Day03-3 Dict练习


student = {
    "name": "凯凯",
    "age": 20,
    "score": 95.5
}


print(student)


print(student["name"])


student["score"] = 98


print(student)


student["major"] = "AI"


print(student)


# Day03-2 条件判断

score = 95

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("需要努力")


# for循环

skills = ["Python", "NumPy", "Pandas", "AI"]

for skill in skills:
    print(skill)


# while循环

count = 1

while count <= 5:
    print("第", count, "次学习Python")
    count = count + 1


# 函数 function

def introduce(name):
    print("我是", name)
    print("正在学习AI")


introduce("凯凯")
introduce("Python学生")


# 函数返回值 return

def calculate_score(score):
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "需要努力"


result = calculate_score(95)

print(result)


# NumPy基础

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(arr * 2)


# NumPy数组属性

import numpy as np

data = np.array([[1,2,3],
                 [4,5,6]])

print(data)

print("数组形状:")
print(data.shape)

print("维度:")
print(data.ndim)

print("元素数量:")
print(data.size)


# NumPy数组计算

import numpy as np

a = np.array([10,20,30])

print("加法:")
print(a + 5)

print("乘法:")
print(a * 2)

print("平方:")
print(a ** 2)


# NumPy数组计算

import numpy as np

a = np.array([10,20,30])

print("原数组:")
print(a)

print("加5:")
print(a + 5)

print("乘2:")
print(a * 2)

print("平方:")
print(a ** 2)



# NumPy统计计算

score = np.array([80,90,100,70,60])

print("平均分:")
print(score.mean())

print("最高分:")
print(score.max())

print("最低分:")
print(score.min())


# NumPy矩阵

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print("矩阵:")
print(matrix)

print("形状:")
print(matrix.shape)

print("维度:")
print(matrix.ndim)


A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

result = np.dot(A, B)
print("矩阵乘法结果:")
print(result)


import pandas as pd


data = {
    "name":["凯凯","小明","小红"],
    "age":[20,21,19],
    "score":[95,88,92]
}


df = pd.DataFrame(data)

print(df)


print("平均分:")
print(df["score"].mean())


print("最高分:")
print(df["score"].max())


print("最低分:")
print(df["score"].min())


print("\n------ Pandas筛选练习 ------")
import pandas as pd

data = {
    "name": ["凯凯", "小明", "小红"],
    "age": [0, 21, 19],
    "score": [95, 88, 92]
}

df = pd.DataFrame(data)

print(df)

print("成绩大于90:")
print(df[df["score"] > 90])

print("只查看姓名和成绩:")
print(df[["name", "score"]])


# if 条件判断

score = 85

if score >= 90:
    print("优秀")
else:
    print("继续努力")


score = 92

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")


name = "凯凯"
score = 96

if name == "凯凯" and score >= 90:
    print("凯凯 成绩优秀")
elif name == "凯凯" and 60 <= score <90:
    print("凯凯 成绩合格")
else:
    print("凯凯 需要努力")


print("-----for循环练习-----")

courses = ["Python", "NumPy", "Pandas", "AI"]

for course in courses:
    print("正在学习:", course)


print("-----次数练习-----")

for i in range(1,6):
    print("第", i, "次学习Python")


scores = [85,92,78,96,88]

def calculate_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

for i in range(len(scores)):
    print("第", i+1, "个学生成绩:", scores[i])
    print( calculate_grade(scores[i]))


count = 1

while count <= 5:
    print("AI学习第", count, "天")
    count += 1


students = [
    {"name":"凯凯","score":95},
    {"name":"小明","score":88},
    {"name":"小红","score":92}
]


def calculate_grade(score):

    if score >= 90:
        return "优秀"

    elif score >=60:
        return "及格"

    else:
        return "不及格"



total = 0
max_score = 0


for student in students:

    name = student["name"]
    score = student["score"]

    print(name, "成绩:", score)
    print(calculate_grade(score))

    total += score

    if score > max_score:
        max_score = score



average = total / len(students)


print("----------------")
print("平均分:", average)
print("最高分:", max_score)

