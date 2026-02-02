

def sum(array):
    def recurse(i, arr, sum):
        if i>= len(arr):
            return sum
        sum += arr[i]
        return recurse(i+1, arr, sum)
    return recurse(0, array, 0)

print (sum([1,2]))
print (sum([1,2,3]))
print (sum([1,2,3]))
print (sum([8,2,2,2,2 ]))
