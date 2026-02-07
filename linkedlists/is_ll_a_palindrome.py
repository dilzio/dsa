# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
'''
Explore
1,2,3,4,3,2,1 -> True
1-> True
1,1 -> True
1,2 - False
1,2,3,3,2,1 -> False
1,2,1 -> True

10,9,5,9,10 -> True
1,2,2,1 -> True



not sorted

Brainstorm:
iterate the list and build an array
solve for palindrome with array
O(2n) + O(n) size
'''


def solution(head):
    arr = []
    while head:
        arr.append(head.value)
        head = head.next

    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True

