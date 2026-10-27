from list_node import ListNode
from operations import delete_value
from operations import reverse_list
from operations import has_cycle

#创建节点
node_a = ListNode(10)
node_b = ListNode(20)
node_c = ListNode(30)

#连接
node_a.next = node_b
node_b.next = node_c

print(node_a.val)
print(node_a.next.val)
print(node_a.next.next.val)
print()


#再链表头部插入新节点
new_node = ListNode(5)

new_node.next = node_a

head_node = new_node

#遍历链表
current_node = head_node

while current_node:
    print(current_node.val)
    current_node = current_node.next

print()


new_tail = ListNode(40)

tail_node = head_node

while tail_node.next:
    tail_node = tail_node.next

tail_node.next = new_tail

current_node_2 = head_node

while current_node_2:
    print(current_node_2.val)
    current_node_2 = current_node_2.next


#删除20
delete_current = head_node

while delete_current.next:
    if delete_current.next.val == 20:
        print("找到了")
        delete_current.next = delete_current.next.next
        break

    delete_current = delete_current.next


check_after_delete = head_node

while check_after_delete:
    print(check_after_delete.val)
    check_after_delete = check_after_delete.next

print()



#测试删除节点5
head_node = delete_value(head_node, 5)
#删除中间节点 30
head_node = delete_value(head_node, 30)

check_delete_middle = head_node

while check_delete_middle:
    print(check_delete_middle.val)
    check_delete_middle = check_delete_middle.next

print()


reverse_a = ListNode(10)
reverse_b = ListNode(20)
reverse_c = ListNode(30)
reverse_d = ListNode(40)

reverse_a.next = reverse_b
reverse_b.next = reverse_c
reverse_c.next = reverse_d

reverse_head = reverse_a

reverse_head = reverse_list(reverse_head)

check_reverse_clean = reverse_head

while check_reverse_clean:
    print(check_reverse_clean.val)
    check_reverse_clean = check_reverse_clean.next

print()

#构建有环链表
cycle_a = ListNode(10)
cycle_b = ListNode(20)
cycle_c = ListNode(30)
cycle_d = ListNode(40)

cycle_a.next = cycle_b
cycle_b.next = cycle_c
cycle_c.next = cycle_d

cycle_d.next = cycle_b

print(has_cycle(cycle_a))
print()


normal_a = ListNode(10)
normal_b = ListNode(20)
normal_c = ListNode(30)
normal_d = ListNode(40)

normal_a.next = normal_b
normal_b.next = normal_c
normal_c.next = normal_d

print(has_cycle(normal_a))
