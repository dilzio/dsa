


def replaceNegValues(array):

       def recurse(index):
           if index >= len(array):
               return
           if array[index] < 0:
               array[index] = array[index] * -1

       recurse(0)
       return array


print(replaceNegValues([-11,1,1]))