#栈和队列

#stack 栈
stack = []

#入栈
stack.append(10)
stack.append(20)
stack.append(30)

#出栈并打印
print("弹出：",stack.pop())

#查看栈顶
print("栈顶：",stack[-1])

#打印栈
print("栈：",stack)



#括号匹配
s = "((("
bracket_stack = []

#引入新变量
brackets_valid = True

#增加对应关系
bracket_pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for char in s:
    if char in ['(', '[', '{']:
        bracket_stack.append(char)
    elif char in [')', ']', '}']:
        if not bracket_stack:
            brackets_valid = False
            print("不匹配")
            break

        if bracket_pairs[char] == bracket_stack[-1]:
            print("匹配")
            bracket_stack.pop()

        else:
            brackets_valid = False
            print("不匹配")
            break

if brackets_valid and not bracket_stack:
    print("括号合法")
else:
    print("括号不合法")

print(bracket_stack)


print()

#队列Queue
from collections import deque

queue_data = deque()

queue_data.append(10)
queue_data.append(20)
queue_data.append(30)

out_value = queue_data.popleft()

print(out_value)
print(queue_data)
print(queue_data[0])
print(queue_data)

print()


#小综合练习

task_queue = deque(["任务A", "任务B", "任务C"])

while task_queue:
    print(f"处理：{task_queue.popleft()}")

print()

#栈 vs 队列对比练习

#初始化栈和队列
compare_stack = []
compare_queue = deque()

#入栈和入列
compare_stack.append("A")
compare_stack.append("B")
compare_stack.append("C")

compare_queue.append("A")
compare_queue.append("B")
compare_queue.append("C")

#各取出一个元素
print("出栈：",compare_stack.pop())
print("出列：",compare_queue.popleft())
