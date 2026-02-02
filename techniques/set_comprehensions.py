#extract unique values from a list of tuples
from collections import Counter

pairs = [(1,'a'),(2,'b'),(3,'a'),(4,'c')]
unique_letters = {letter for _, letter in pairs if letter in ['b','c']}
print(unique_letters)


#filtering while deduplicating
nums = [1,2,3,4,5,6,6,2,3]
evens = {x for x in nums if x % 2 == 0}
print(evens)


#find distinct kth highest
k = 2
pairs = [("I",2),("you",2),("them",8),("cow",1),("it",5)]

occurrences_of_k = {(letter,count) for letter, count in pairs if count == k}
print(occurrences_of_k)

#extract distinct frequencies from a counter
c1 = Counter("bananan")
k= 3 #return the second most common letter with frequncy (n,2)
most_common = c1.most_common()
print(most_common)
#get distinct k values and filter
distinctvals_list = [count for _,count in most_common if count == k]
distinctvals_set = {count for _,count in most_common if count == k}
print(distinctvals_list, distinctvals_set)

#transform (reverse here) while deduping
words = ['foo', 'foo', 'bar', 'baz']
print({word[::-1] for word in words})

#cartesian product
A = [1,2,3,4]
B = [1,2,3]
cells = {(a,b) for a in A for b in B}
#sort cells by rank and file
print(sorted(cells))
#sort cells by rank and -file
print(sorted(cells, key= lambda t:(t[0], -t[1])))
