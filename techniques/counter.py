from collections import Counter

c1 = Counter('aabcd')
for i in c1.elements():
    print(i)

c2 = Counter([1,2,2,2,2,2,5,5,6,6])
for i in c2.elements():
    print(i)
print(c2.most_common()[::-2])

#get kth distinct frequency
c3 = Counter([1,2,2,2,2,2,5,5,6,6])
k = 2
freqs = c3.most_common()
#Step 1 extract distinct frequencies in descending order
distinct_frequencies = sorted({}, reverse=True)
print()

c4 = Counter("foo")
c5 = Counter("baro")
print(c4 | c5) #Take maximum count per key
print(c4 & c5) #Take minimum count per key, where key exists in both
print(c4 + c5) #Add each element from two sets (elements in one set keep their value
print(c4 - c5) #Subtract - values with 0 or less are removed
c4.subtract(c5) #Subtract - but allows negative numbers
print(c4)
c4a = Counter("baz")
c4.update(c4a) #like += - adds elements of c4a to c4
print (c4)
c6 = Counter({'x':1} )
c7 = Counter({'x':1} )
print(c6 == c7)
print((c4 -c5) +(c5-c4)) #symmetric difference

c8 = Counter({'x':1, 'y':0, 'z':-1} )   #strips out 0 and negative values
print(f'before: {c8}')
c8 += Counter()
print(f'after: {c8}')

print(c4.total())

