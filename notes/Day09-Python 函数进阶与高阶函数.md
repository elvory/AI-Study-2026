---
tags:
  - 主题/Python
  - 类型/每日笔记
aliases:
  - "Day09"
---

![[Pasted image 20260903125625.png]]

# Day09 - Python 函数进阶与高阶函数

## 今日学习内容

- 默认参数
- 位置参数与关键字参数
- `*args`
- `**kwargs`
- 参数解包 `*`
- 字典解包 `**`
- 函数作为变量
- 函数作为参数
- 高阶函数
- `map()`
- `filter()`
- `lambda`
- 装饰器 Decorator 基础

---

# 1. 默认参数

函数参数可以设置默认值。

```python
def greet(name="User"):
    print(f"Hello {name}")
```

调用：

```python
greet()
```

输出：

```text
Hello User
```

调用：

```python
greet("Tom")
```

输出：

```text
Hello Tom
```

## 注意

默认参数一般放在普通参数后面。

正确：

```python
def test(a, b=10):
    pass
```

错误：

```python
def test(a=10, b):
    pass
```

---

# 2. 位置参数与关键字参数

定义：

```python
def student_info(name, age):
    print(name, age)
```

## 位置参数

```python
student_info("Alice", 20)
```

按照位置传递：

```text
name = "Alice"
age = 20
```

## 关键字参数

```python
student_info(
    name="Alice",
    age=20
)
```

按照参数名字传递。

---

# 3. *args

`*args` 用于：

> 接收任意数量的位置参数。

例如：

```python
def calculate_sum(*args):
    return sum(args)

print(calculate_sum(1, 2, 3, 4, 5))
```

输出：

```text
15
```

函数内部：

```python
args
```

实际上是：

```python
(1, 2, 3, 4, 5)
```

类型：

```text
tuple
```

## 核心理解

```text
*args
↓
接收任意数量的位置参数
↓
函数内部变成 tuple
```

---

# 4. **kwargs

`**kwargs` 用于：

> 接收任意数量的关键字参数。

例如：

```python
def show_student(**kwargs):
    print(kwargs)

show_student(
    name="Alice",
    age=20,
    grade="A"
)
```

输出：

```python
{
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

函数内部：

```python
kwargs
```

是：

```text
dict
```

## 遍历 kwargs

```python
def show_student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
```

---

# 5. *args 和 **kwargs 对比

```text
*args
↓
接收位置参数
↓
tuple
```

```text
**kwargs
↓
接收关键字参数
↓
dict
```

快速记忆：

```text
*     → 位置参数
**    → 关键字参数
```

---

# 6. 列表 / 元组参数解包 *

假设：

```python
numbers = [1, 2, 3]
```

函数：

```python
def add(a, b, c):
    return a + b + c
```

可以：

```python
add(*numbers)
```

等价于：

```python
add(1, 2, 3)
```

## print 中的应用

```python
numbers = [1, 2, 3]

print(*numbers)
```

输出：

```text
1 2 3
```

而：

```python
print(numbers)
```

输出：

```text
[1, 2, 3]
```

---

# 7. 字典参数解包 **

例如：

```python
student = {
    "name": "Alice",
    "age": 20,
    "score": 90
}
```

函数：

```python
def create_student(name, age, score):
    print(
        f"Name: {name}, Age: {age}, Score: {score}"
    )
```

调用：

```python
create_student(**student)
```

等价于：

```python
create_student(
    name="Alice",
    age=20,
    score=90
)
```

## 核心理解

```text
字典
↓
** 解包
↓
关键字参数
```

---

# 8. 函数可以赋值给变量

Python 中函数也是对象。

定义：

```python
def say_hi():
    print("Hi!")
```

可以：

```python
func = say_hi
```

然后：

```python
func()
```

输出：

```text
Hi!
```

## 注意

```python
func = say_hi
```

表示：

> 把函数本身保存给 func。

而：

```python
func = say_hi()
```

表示：

> 立即执行 say_hi()，然后把返回值保存给 func。

所以：

```text
say_hi
↓
函数本身
```

```text
say_hi()
↓
调用函数
```

---

# 9. 函数可以作为参数

例如：

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

再定义：

```python
def calculate(func, a, b):
    return func(a, b)
```

调用：

```python
print(calculate(add, 3, 5))
print(calculate(multiply, 3, 5))
```

输出：

```text
8
15
```

第一次：

```python
calculate(add, 3, 5)
```

相当于：

```text
func = add
a = 3
b = 5
```

然后：

```python
func(a, b)
```

相当于：

```python
add(3, 5)
```

---

# 10. 高阶函数 Higher-order Function

高阶函数可以理解为：

> 接收函数作为参数，或者返回函数的函数。

例如：

```python
def calculate(func, a, b):
    return func(a, b)
```

这里：

```python
func
```

就是一个函数参数。

所以 `calculate()` 是一个高阶函数。

---

# 11. map()

`map()` 用于：

> 对可迭代对象中的每个元素执行同一个函数。

例如：

```python
numbers = [1, 2, 3, 4, 5]

result = list(
    map(
        lambda x: x * 2,
        numbers
    )
)

print(result)
```

输出：

```python
[2, 4, 6, 8, 10]
```

## 理解

```text
1 → 2
2 → 4
3 → 6
4 → 8
5 → 10
```

所以：

```text
map()
↓
遍历
+
转换
```

---

# 12. filter()

`filter()` 用于：

> 根据条件筛选数据。

例如：

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(result)
```

输出：

```python
[2, 4, 6, 8]
```

这里：

```python
lambda x: x % 2 == 0
```

会返回：

```text
True / False
```

`filter()`：

```text
True  → 保留
False → 丢弃
```

---

# 13. map() 和 filter() 对比

```text
map()
↓
转换数据
```

```text
filter()
↓
筛选数据
```

例如：

```python
map(lambda x: x * 2, numbers)
```

表示：

> 每个数字乘 2。

而：

```python
filter(lambda x: x % 2 == 0, numbers)
```

表示：

> 只保留偶数。

---

# 14. lambda 回顾

基本结构：

```python
lambda 参数: 返回值
```

例如：

```python
lambda x: x * 2
```

意思：

> 接收 x，返回 x * 2。

例如：

```python
lambda student: student[1]
```

意思：

> 接收 student，返回 student[1]。

---

# 15. lambda 与高阶函数

例如：

```python
sorted(
    students,
    key=lambda student: student[1]
)
```

这里：

```python
lambda student: student[1]
```

是一个函数。

而：

```python
sorted()
```

接收这个函数作为 `key`。

所以这里也体现了高阶函数思想。

---

# 16. 装饰器 Decorator

装饰器的作用：

> 在不修改原函数核心代码的情况下，为函数增加额外功能。

以后经常会看到：

```python
@app.get("/")
```

或者：

```python
@timer
```

这样的写法。

---

# 17. 函数嵌套

函数内部可以定义函数。

```python
def outer():

    def inner():
        print("Hello")

    inner()
```

调用：

```python
outer()
```

输出：

```text
Hello
```

---

# 18. 函数返回函数

```python
def outer():

    def inner():
        print("Hello")

    return inner
```

调用：

```python
func = outer()

func()
```

输出：

```text
Hello
```

这里：

```python
return inner
```

表示：

> 返回 inner 函数本身。

---

# 19. return wrapper 和 wrapper() 的区别

这是今天非常重要的一个点。

```python
return wrapper
```

表示：

> 返回 wrapper 函数本身，不执行。

而：

```python
return wrapper()
```

表示：

> 先执行 wrapper，再返回 wrapper 的执行结果。

快速记忆：

```text
wrapper
↓
函数本身
```

```text
wrapper()
↓
执行函数
```

---

# 20. 基础装饰器结构

```python
def my_decorator(func):

    def wrapper():
        print("前面")

        func()

        print("后面")

    return wrapper
```

使用：

```python
@my_decorator
def hello():
    print("Hello")
```

调用：

```python
hello()
```

输出：

```text
前面
Hello
后面
```

---

# 21. @语法的本质

下面：

```python
@my_decorator
def hello():
    print("Hello")
```

本质上相当于：

```python
hello = my_decorator(hello)
```

而：

```python
my_decorator(hello)
```

返回：

```python
wrapper
```

因此：

```text
hello
↓
最后指向 wrapper
```

调用：

```python
hello()
```

实际上就是调用：

```python
wrapper()
```

---

# 22. 支持参数的装饰器

如果原函数有参数：

```python
def add(a, b):
    print(a + b)
```

装饰器的 `wrapper()` 也应该能够接收参数：

```python
def my_decorator(func):

    def wrapper(*args, **kwargs):

        print("前面")

        result = func(*args, **kwargs)

        print("后面")

        return result

    return wrapper
```

使用：

```python
@my_decorator
def add(a, b):
    return a + b
```

调用：

```python
print(add(3, 5))
```

---

# 23. 为什么装饰器里会出现 *args 和 **kwargs

因为装饰器并不知道：

> 原函数到底会接收多少参数。

所以：

```python
def wrapper(*args, **kwargs):
```

可以统一接收：

```text
任意数量位置参数
+
任意数量关键字参数
```

然后再：

```python
func(*args, **kwargs)
```

把参数继续传给原函数。

---

# 24. Day09 综合知识链

```text
普通函数
↓
参数
↓
默认参数
↓
*args / **kwargs
↓
参数解包
↓
函数也是对象
↓
函数可以赋值
↓
函数可以作为参数
↓
高阶函数
↓
lambda
↓
map / filter / sorted
↓
函数可以返回函数
↓
Decorator
```

---

# 25. 今日踩坑 / 易混点

## 1. *args 和 **kwargs

```text
*args
↓
tuple
```

```text
**kwargs
↓
dict
```

---

## 2. * 和 ** 解包

```text
*列表 / 元组
↓
位置参数解包
```

```text
**字典
↓
关键字参数解包
```

---

## 3. 函数本身与调用函数

```python
func = say_hi
```

是：

```text
保存函数
```

而：

```python
func = say_hi()
```

是：

```text
执行函数并保存返回值
```

---

## 4. map 和 filter

```text
map
↓
转换
```

```text
filter
↓
筛选
```

---

## 5. return wrapper

```python
return wrapper
```

返回：

```text
函数本身
```

不是：

```text
函数执行结果
```

---

# 26. 今日快速记忆

```text
*args
任意数量位置参数
内部是 tuple


**kwargs
任意数量关键字参数
内部是 dict


*data
位置参数解包


**data
关键字参数解包


函数名
函数本身


函数名()
执行函数


高阶函数
接收函数 / 返回函数


map()
数据转换


filter()
数据筛选


lambda
匿名小函数


decorator
给函数增加额外功能


@decorator
相当于：
function = decorator(function)
```

---

# 27. Day09 完成情况

- [x] 默认参数
- [x] 位置参数
- [x] 关键字参数
- [x] `*args`
- [x] `**kwargs`
- [x] `*` 参数解包
- [x] `**` 字典解包
- [x] 函数作为变量
- [x] 函数作为参数
- [x] 高阶函数
- [x] `map()`
- [x] `filter()`
- [x] `lambda` 回顾
- [x] 函数嵌套
- [x] 函数返回函数
- [x] Decorator 基础
- [x] `return wrapper` 与 `wrapper()` 区别

# Day09 完成 ✅

---

## 知识关联

- 主题入口：[[maps/Python基础|Python基础]]
