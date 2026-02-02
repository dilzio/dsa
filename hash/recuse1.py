


def findNumber(array, number):
       def recurse(index, number):
            if index == len(array) - 1:
                return False
            if array[index] == number:
                return True
            recurse(index + 1, number)

            return False

       return recurse(0, number)


print(findNumber([1,2,3], 0))