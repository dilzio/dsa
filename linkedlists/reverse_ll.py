class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        nxt = curr.next      # 1. save next
        curr.next = prev     # 2. reverse pointer
        prev = curr          # 3. advance prev
        curr = nxt           # 4. advance curr

    return prev


result = reverse_list(ListNode(1,ListNode(2,ListNode(3))))
print(result)
