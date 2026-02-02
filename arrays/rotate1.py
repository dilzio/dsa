

def rotateWords(string, k):
    words = string.split()
    n = len(words)
    if n == 0:
        return string

    k = k % n

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    #Reverse whole list
    reverse(words, 0, n -1)

    #Reverse prefix (first k words)
    reverse(words, 0, k-1)

    #Reverse suffix (n - k words)
    reverse(words,k, n-1)


    return " ".join(words)

'''
print(rotateWords("I am cool", 1))
print(rotateWords("I am cool", 2))
print(rotateWords("I am cool", 3))
'''

def rotateArray(array):
    if not array:
        return []
    retArr = []

    start = 0
    for i, val in enumerate(array):
        if val == 0 or i == len(array):
            retArr.append(reverse(array, start, i-1))
            start = i

    return retArr

def reverse(array, start, end):
    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
    return array


# print(rotateArray([1,2,0,3,4]))


'''
In this variation, you will be receiving an array of Int, where the number 0 represents a word break. Reverse all the elements between the 0s
'''
def revChunks(arr):
    ret = []
    tokens = get_chunks(arr)
    for token in tokens:
        token.reverse()
        for c in token:
            ret.append(c)
    return ret

def get_chunks(arr):
    ret = []
    chunk = []
    for x in arr:
        if x == 0:
            if chunk:
                ret.append(chunk)
                chunk = []
        else:
            chunk.append(x)
    if chunk:
        ret.append(chunk)
    return ret

# print(revChunks([1,2,3]) == [3,2,1])
#print(revChunks([1,2,3,0,4,5,6]) == [3,2,1,6,5,4])
# print(revChunks([1,2,3,0,4,5,6,0]) == [3,2,1,6,5,4])

#Rotate words by x

'''
pLan:
tokenize string
normalize k to get offset
create a deque
load elements into deque, pop() from end and push() in front k times
'''
from collections import *
def rotate(string, k):
    words = string.split()
    k = k % len(string)
    rotatedD = deque(words)
    for i in range(k):
        val = rotatedD.pop()
        rotatedD.appendleft(val)
    return " ".join(rotatedD)


print(rotate("I am a dog", 4))


