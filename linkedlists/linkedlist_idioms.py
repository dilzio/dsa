
from types import SimpleNamespace
Node = lambda val=None, next=None: SimpleNamespace(val=val, next=next)

print(Node(1,Node(2, Node(3))))


# return a list of val fields
def iterlist(head):
    while head:
        yield head.val
        head = head.next


print([val for val in iterlist(Node(1, Node(2, Node(3))))])

#remove node at index i
def removeAtI(head, index):
    counter = 0
    dummy = Node(-1)
    dummy.next = head
    current = head
    previous = dummy
    while current:
        if counter == index:
            previous.next = current.next
        previous = current
        current = current.next
        counter += 1
    return dummy.next

head = Node(1, Node(2, Node(3)))
i = 2
newHead = removeAtI(head, i)
print (removeAtI(head, i))

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
i = 3
newHead = removeAtI(head, i)
print (removeAtI(head, i))


def removeItemsAtIndex(head, indexlist):
    dummy = Node(-1)
    dummy.next = head
    arypos = 0
    current = head
    previous = dummy
    listpos = 0
    while current and arypos < len(indexlist):
        if listpos == indexlist[arypos]:
            previous.next = current.next
            arypos += 1
        else:
            previous  = current
        listpos += 1
        current = current.next
    return dummy.next


result = removeItemsAtIndex(Node(1, Node(2, Node(3))), [0,2])
print(result)


result = removeItemsAtIndex(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))),[1,2])

print (result)



