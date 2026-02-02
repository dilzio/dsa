#compare intersection of two lists

#return all elements of active users found in paid users - it ignores counts
active_users = [101, 102, 103, 103, 104]
paid_users   = [103, 104, 105]

paid_and_active = [x for x in active_users if x in set(paid_users)]
print(paid_and_active)

#difference - find elements that were in last week but
last_week = [1, 2, 3, 4, 5, 1]
this_week = [3, 4, 5]
print([x for x in last_week if x not in this_week])

#xor
group_a = [1, 2, 3]
group_b = [3, 4, 5]

print(list(set(group_a) ^ set(group_b)))
print("-" * 10)


#compute rolling sums of size k
nums = [1, 2, 3, 4, 5]
k = 3

windows = [sum(nums[i:i+k]) for i in range(len(nums)- k + 1)]
print(range(len(nums) - k + 1))
print(windows)

print("-" * 10)
k=3
myarr = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(myarr) - k +1):
    print(myarr[i])

#find the biggest contiguous subarray of size

nums = [10,1,100,50,30,200]
k = 3

#calulate sums:
sums = [sum(nums[i:i+k]) for i in range(len(nums) - k + 1)]
print(sums)
print (max(sums))
