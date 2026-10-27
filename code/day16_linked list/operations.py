from list_node import ListNode
#合成函数

def delete_value(head,target):
    if head is None:
        return None

    if head.val == target:
        return head.next

    current_delete = head

    while current_delete.next:
         if current_delete.next.val == target:
                current_delete.next=current_delete.next.next
                break

                current_delete = current_delete.next

    return head


#反转链表
#需要三个指针
#prev 前一个节点
#current 当前正在处理的节点
#next_node 先保存原来的下一个节点

def reverse_list(head):
     prev = None
     current = head

     while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

     return prev


#快慢指针找中点
#slow,fast两个指针
#fast走的速度是slow的两倍,fast走到终点，slow刚好是中点

def find_middle(head):

     slow = head
     fast = head

     while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

     return slow

reverse_a = ListNode(10)
reverse_b = ListNode(20)
reverse_c = ListNode(30)
reverse_d = ListNode(40)

reverse_a.next = reverse_b
reverse_b.next = reverse_c
reverse_c.next = reverse_d

reverse_head = reverse_a

reverse_head = reverse_head

check_reverse_clean = reverse_head

while check_reverse_clean:
    print(check_reverse_clean.val)
    check_reverse_clean = check_reverse_clean.next


middle_node = find_middle(reverse_head)
print(middle_node.val)

#链表有环
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
         slow = slow.next
         fast = fast.next.next

         if slow == fast:
              return True
    return False
