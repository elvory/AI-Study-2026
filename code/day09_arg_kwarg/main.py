#接受任意数量的参数并返回它们的和
def calculate_sum(*args):
    return sum(args)

# 示例用法
result = calculate_sum(1, 2, 3, 4, 5)
print(result)  # 输出: 15

def show_student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 示例用法
show_student(name="Alice", age=20, grade="A")


student={
    "name":"Alice",
    "age":20,
    "score":90
}

def create_student(name, age, score):
    print(f"Name: {name}, Age: {age}, Score: {score}")

create_student(**student)



def say_hi():
    print("Hi!")

func = say_hi
func()  # 输出: Hi!


def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def calculate(func,a,b):
    return func(a,b)

print(calculate(add,3,5))
print(calculate(multiply,3,5))


numbers_1=[1,2,3,4,5]
num_1=list(map(lambda x:x*2,numbers_1))
print(num_1)


numbers_2=[1,2,3,4,5,6,7,8]
num_2=list(filter(lambda x:x%2==0,numbers_2))
print(num_2)
