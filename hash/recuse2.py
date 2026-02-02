


def countNumber(array, number):

       def recurse(index, counter):
            if array[index] == number:
                counter += 1
            recurse(index + 1)
            return counter
       return recurse(0,0)

print(countNumber([1,2,3], 1))