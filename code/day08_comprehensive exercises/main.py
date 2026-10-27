numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

uneven_numbers = [num for num in numbers if num %2 != 0]

print(f"奇数列表: {uneven_numbers}")
print()

squares = [num ** 2 for num in numbers if num % 2 == 0]

print(f"偶数的平方列表: {squares}")


numbers_1 = [1, 2, 3, 4, 5, 6]

squares_1 = {num: num **2 for num in numbers_1 if num % 2 == 0}
print(f"偶数的平方字典: {squares_1}")

students = ["Alice", "Bob", "Charlie", "David"]

for i, name in enumerate(students):
    print(i, name)
#enumerate()函数用于在迭代时获取元素的索引和值，返回一个可迭代的对象，每次迭代返回一个包含索引和值的元组。enumerate() 默认从 0 开始，但也可以指定起始编号,后加上一个参数 start 来指定起始编号。(students, start=1) 这样就可以从 1 开始编号。


products = ["苹果", "香蕉", "橙子"]
prices = [5, 3, 6]

for product, price in zip(products, prices):
    print(product, price)
# zip() 将多个可迭代对象中对应位置的元素组合成元组，
# 并返回一个迭代器。
## 如果两个列表长度不一样，zip() 会以较短的那个为准。


#sorted(numbers),会返回一个新的列表，不会修改原来的 numbers。

scores = [88, 95, 72, 100, 85]
sorted_scores = sorted(scores, reverse = True) # reverse = True 表示降序排列，默认为升序排列。
print(sorted_scores)


#key =  告诉 sorted “拿什么东西作为排序依据

students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72),
    ("David", 100)
]


def get_score(student):
    return student[1]

#按成绩从高到低排序
sorted_students = sorted(students, key=get_score, reverse=True)
print(sorted_students)

sorted_students_1 = sorted(students, key=lambda student : student[1], reverse=True)
print(sorted_students_1)

