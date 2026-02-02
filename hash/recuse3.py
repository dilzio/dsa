


def calcMean(array):
       sum = 0

       def recurse(index):
           if index >= len(array):
               return sum
           recurse(index + 1)
           sum += array[index]
       return recurse(0) // len(array)


print(calcMean([1,1,1]))