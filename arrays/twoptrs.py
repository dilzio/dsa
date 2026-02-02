'''
Two Pointer Algo Examples
O(n) time (where n may be the length of the longest of multiple arrays
O(1) space
'''
from typing import List


def ispalindrome(array:str):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] != array[right]:
            return False
        left += 1
        right -= 1
    return True



print (ispalindrome("racecar"))
print (ispalindrome("fussy"))
'''
works if array is sorted
'''
def findSumInArray(array:int, target:int):
    left = 0
    right = len(array)-1
    while left < right:
        sum = array[left]+array[right]
        if sum == target:
            return True
        if sum < target:
            left += 1
        if sum > target:
            right -= 1
    return False
print(findSumInArray([1,3,4], 2))


'''
Use a 2 pointer approach on 2 sorted arrays
'''
def merge2Arrays(arr1: int, arr2: int) -> int:
    answer = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            answer.append(arr1[i])
            i += 1
        else:
            answer.append(arr2[j])
            j += 1

    while i < len(arr1):
        answer.append(arr1[i])
        i += 1

    while j < len(arr2):
        answer.append(arr2[j])
        j += 1

    return answer


print(merge2Arrays([1,4,6],[2,3,5]))
print(merge2Arrays([2,8,10],[1,3,5,12,13]))

'''
Find a subsequence of a string in another string

'''
def findSubSeq(target: str, sub: str) -> bool:
    i = 0
    j = 0

    while i < len(target) and j<len(sub):
        if target[i] == sub[j]:
            j +=1
        i += 1
    if i==len(sub):
        return True

    return False

print(findSubSeq("fucker", "fuck"))
print(findSubSeq("fucker", "fug"))

'''
reverse a string
'''
def reverse(arr: List)-> None:
    i=0
    j=len(arr)-1

    while i < j:
        arr[i], arr[j] = arr[j],arr[i]
        i += 1
        j -= 1


test = ['a','b','c', 'd', 'e', 'f', 'g']
reverse(test)
print (test)

'''
retun a sorted list of squares of number in a sorted list
brute force (o n log n) would be to sort the array of squares
'''

def sortSquares(A: List[int]):
    return_array = [0] * len(A)
    write_pointer = len(A) - 1
    left_read_pointer = 0
    right_read_pointer = len(A) - 1
    left_square = A[left_read_pointer] ** 2
    right_square = A[right_read_pointer] ** 2
    while write_pointer >= 0:
        if left_square > right_square:
            return_array[write_pointer] = left_square
            left_read_pointer += 1
            left_square = A[left_read_pointer] ** 2
        else:
            return_array[write_pointer] = right_square
            right_read_pointer -= 1
            right_square = A[right_read_pointer] ** 2
        write_pointer -= 1
    return return_array

print (sortSquares([-4,-3,-2,0,1,2]))