def return_middle(head):
    fast = head
    slow = head


    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

from types import SimpleNamespace
Node = lambda val=None, next=None: SimpleNamespace(val=val, next=next)



print(return_middle(None))
print(return_middle(Node(1)))
print(return_middle(Node(1,Node(2))))
print(return_middle(Node(1,Node(2, Node(3)))))
print(return_middle(Node(1,Node(2, Node(3, Node(4))))))
print(return_middle(Node(1,Node(2, Node(3, Node(4, Node(5)))))))

