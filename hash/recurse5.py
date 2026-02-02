


def reverse(array):

       def recurse(index):

           def recurse(index):
               if index >= len(array):
                   return array
               if array[index] < 0:
                   array[index] = 0
               return recurse(index + 1)

           recurse(0)
           return array


print(replaceNegValues([-11,1,1]))