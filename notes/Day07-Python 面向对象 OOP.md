---
tags:
  - 主题/Python
  - 类型/每日笔记
aliases:
  - "Day07"
---

![[Pasted image 20260831231951.png]]
# Day07｜Python 面向对象 OOP

## 一、今日目标

掌握 Python 面向对象编程（OOP）的核心概念：

- 类（Class）
- 对象（Object）
- `self`
- `__init__`
- 实例属性
- 实例方法
- 继承（Inheritance）
- `super()`
- 方法重写（Override）
- 多态（Polymorphism）
- `isinstance()`
- `type()`
- `match / case`
- 结构化模式匹配
- 不同类型对象的统一处理

---

# 二、类与对象

## 1. 类 Class

类可以理解为创建对象的模板。

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("成绩：", self.score)
```

## 2. 对象 Object

根据类创建出来的具体实例叫对象。

```python
s1 = Student("Bob", 20, 75)
s2 = Student("Alice", 21, 90)
```

关系：

```text
Student → 类
s1      → Student 的对象
s2      → Student 的对象
```

---

# 三、self

`self` 表示当前正在操作的对象。

例如：

```python
s1.show_info()
```

可以理解成：

```python
Student.show_info(s1)
```

所以：

```python
self.name
```

表示：

> 当前对象的 `name` 属性。

---

# 四、__init__

`__init__()` 是对象创建时自动执行的初始化方法。

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
```

创建对象：

```python
s1 = Student("Bob", 20, 75)
```

相当于初始化：

```text
name = Bob
age = 20
score = 75
```

之后可以访问：

```python
s1.name
s1.age
s1.score
```

---

# 五、实例属性与实例方法

## 实例属性

写在 `self` 上的属性：

```python
self.name
self.age
self.score
```

每个对象都有自己独立的属性。

例如：

```python
s1.name
s2.name
```

可以不同。

## 实例方法

定义在类里面，并使用 `self` 的方法：

```python
def show_info(self):
    print(self.name)
```

---

# 六、继承 Inheritance

子类可以继承父类的属性和方法。

```python
class GraduateStudent(Student):
    pass
```

表示：

```text
GraduateStudent
       ↓
     Student
```

`GraduateStudent` 是 `Student` 的子类。

因此它可以使用 `Student` 中已经定义的属性和方法。

---

# 七、super()

`super()` 可以调用父类的方法。

例如：

```python
class GraduateStudent(Student):
    def __init__(self, name, age, score, thesis_title):
        super().__init__(name, age, score)
        self.thesis_title = thesis_title
```

这里：

```python
super().__init__(name, age, score)
```

表示调用父类 `Student` 的 `__init__()`。

这样就不用重复写：

```python
self.name = name
self.age = age
self.score = score
```

---

# 八、方法重写 Override

子类可以重新定义父类已经存在的方法。

父类：

```python
class Student:
    def show_info(self):
        print("=== 学生信息 ===")
```

子类：

```python
class GraduateStudent(Student):
    def show_info(self):
        print("=== 研究生信息 ===")
```

这叫：

> 方法重写（Method Overriding）

子类对象调用 `show_info()` 时，会优先使用子类自己的版本。

---

# 九、多态 Polymorphism

多态是 Day07 最重要的概念之一。

不同的类可以拥有同名方法：

```python
class Student:
    def show_info(self):
        print("这是学生")


class GraduateStudent(Student):
    def show_info(self):
        print("这是研究生")


class Teacher:
    def show_info(self):
        print("这是教师")
```

然后可以把不同类型的对象放到同一个列表：

```python
people = [s1, s2, teacher]
```

统一处理：

```python
for person in people:
    person.show_info()
```

虽然 `person` 实际指向不同类型的对象：

```text
Student
GraduateStudent
Teacher
```

但是都可以调用：

```python
person.show_info()
```

每个对象会执行自己的 `show_info()`。

## 核心理解

> 同一个方法调用，不同对象表现出不同的行为。

这就是多态。

---

# 十、鸭子类型 Duck Typing

Python 很强调一种思想：

> 不关心对象是什么类型，只关心它有没有需要的方法。

例如：

```python
def print_student_info(person):
    person.show_info()
```

这个函数不需要判断：

```python
isinstance(person, Student)
```

只要传入的对象有：

```python
show_info()
```

就可以正常工作。

例如：

```python
print_student_info(s1)
print_student_info(s2)
print_student_info(teacher)
```

这体现了 Python 的鸭子类型思想。

---

# 十一、isinstance()

`isinstance()` 用于判断对象是否属于某个类或其子类。

```python
isinstance(s1, Student)
```

返回：

```python
True
```

对于：

```python
s2 = GraduateStudent(...)
```

因为：

```text
GraduateStudent
       ↓
     Student
```

所以：

```python
isinstance(s2, GraduateStudent)
# True

isinstance(s2, Student)
# True
```

研究生同时也是学生。

---

# 十二、isinstance() 的判断顺序

如果存在继承关系：

```text
GraduateStudent
       ↓
     Student
```

判断时应该：

```python
if isinstance(person, GraduateStudent):
    print("这是研究生")

elif isinstance(person, Student):
    print("这是普通学生")
```

而不是：

```python
if isinstance(person, Student):
    print("这是普通学生")

elif isinstance(person, GraduateStudent):
    print("这是研究生")
```

因为：

```python
isinstance(s2, Student)
```

对于研究生也会返回：

```python
True
```

所以会提前进入 `Student` 分支。

## 记忆

> 有继承关系时，判断子类要放在父类前面。

---

# 十三、type()

`type()` 可以查看对象的实际类型。

```python
print(type(s1))
print(type(s2))
print(type(teacher))
```

可能得到：

```text
<class 'student.Student'>
<class 'student.GraduateStudent'>
<class 'student.Teacher'>
```

简单理解：

```text
type()
→ 这个对象具体是什么类型？

isinstance()
→ 这个对象是不是某个类型体系中的对象？
```

实际判断对象类型时，通常更推荐使用 `isinstance()`。

---

# 十四、match / case

Python 可以使用 `match / case` 根据对象进行匹配。

```python
def check_person(person):
    match person:
        case GraduateStudent():
            print("这是研究生")

        case Student():
            print("这是普通学生")

        case Teacher():
            print("这是教师")

        case _:
            print("未知类型")
```

其中：

```python
case _:
```

表示其他情况。

注意：

```text
GraduateStudent
       ↓
     Student
```

所以同样应该：

> 子类放前面，父类放后面。

---

# 十五、结构化模式匹配

`match / case` 不仅可以判断类型，还可以匹配对象内部属性。

例如：

```python
match person:
    case GraduateStudent(
        name=name,
        age=age,
        score=score,
        thesis_title=thesis_title
    ):
        print(name, age, score, thesis_title)
```

这里可以同时：

1. 判断对象是不是 `GraduateStudent`
2. 获取对象中的属性

这是 Python 比较高级的模式匹配功能。

---

# 十六、不同类型对象放进同一个列表

不同类的对象可以放在同一个列表：

```python
s1 = Student("Bob", 20, 75)

s2 = GraduateStudent(
    "Alice",
    24,
    95,
    "AI Research"
)

teacher = Teacher("Tom", "Python")

people = [s1, s2, teacher]
```

然后统一处理：

```python
for person in people:
    person.show_info()
```

这正好体现：

```text
不同对象
    ↓
同一个列表
    ↓
统一遍历
    ↓
同一个方法调用
    ↓
不同对象执行不同实现
```

---

# 十七、综合函数：统一展示人员信息

可以写：

```python
def show_all_people(people):
    for person in people:
        person.show_info()
        print()
```

调用：

```python
show_all_people(people)
```

这里不需要判断：

```python
Student？
GraduateStudent？
Teacher？
```

直接：

```python
person.show_info()
```

即可。

这就是多态的实际应用。

---

# 十八、综合函数：统计人员角色

例如：

```python
def count_roles(people):
    student_count = 0
    graduate_count = 0
    teacher_count = 0

    for person in people:
        if isinstance(person, GraduateStudent):
            graduate_count += 1

        elif isinstance(person, Student):
            student_count += 1

        elif isinstance(person, Teacher):
            teacher_count += 1

    print(f"普通学生：{student_count}")
    print(f"研究生：{graduate_count}")
    print(f"教师：{teacher_count}")
```

例如：

```python
people = [s1, s2, s3, teacher]

count_roles(people)
```

输出：

```text
普通学生：1
研究生：2
教师：1
```

这个练习综合使用了：

- 类
- 对象
- 继承
- `isinstance()`
- 列表
- `for` 循环
- 条件判断

---

# 十九、print() 与 return

需要注意：

```python
def show_people(people):
    for person in people:
        person.show_info()
```

这个函数没有 `return`。

所以：

```python
print(show_people(people))
```

最终会出现：

```text
None
```

因为 Python 函数如果没有显式 `return`：

```python
return None
```

因此：

```python
show_people(people)
```

和：

```python
print(show_people(people))
```

用途不同。

## 简单记忆

```text
print()
→ 把东西显示出来

return
→ 把结果交给调用者
```

---

# 二十、Day07 核心知识关系

```text
OOP
│
├── 类 Class
│   ├── __init__
│   ├── 属性
│   └── 方法
│
├── 对象 Object
│   └── self
│
├── 继承
│   ├── 子类
│   └── super()
│
├── 方法重写
│
├── 多态 ⭐
│   └── 同一个方法，不同对象，不同行为
│
├── isinstance()
│
├── type()
│
└── match / case
    └── 结构化模式匹配
```

---

# 二十一、Day07 最重要的 5 句话

1. **类是创建对象的模板，对象是类的具体实例。**

2. **`self` 表示当前对象。**

3. **继承让子类获得父类的属性和方法，`super()` 可以调用父类方法。**

4. **方法重写允许子类改变父类已有方法的行为。**

5. **多态就是同样的方法调用，不同对象表现出不同的行为。**

---

# 二十二、Day07 完成情况

- [x] 类与对象
- [x] `self`
- [x] `__init__`
- [x] 实例属性
- [x] 实例方法
- [x] 继承
- [x] `super()`
- [x] 方法重写
- [x] 多态
- [x] 鸭子类型
- [x] `isinstance()`
- [x] `type()`
- [x] `match / case`
- [x] 结构化模式匹配
- [x] 不同类型对象统一处理
- [x] OOP 综合练习

## Day07：✅ 完成

---

## 知识关联

- 主题入口：[[maps/Python基础|Python基础]]
