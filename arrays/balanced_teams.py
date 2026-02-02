def canFormBalancedTeams(array, k):
    if not array:
        return k == 0
    totalpoints = sum(array)
    target = totalpoints // k
    if totalpoints % k != 0:
        return False
    teams = [0] * k
    array = sorted(array, reverse=True )
    n = len(array)
    if array[0] > totalpoints:
        return False

    def backtrack(arrayidx):
        if arrayidx >= n:
            return True  # we are done
        currentSkill = array[arrayidx]
        for i in range(k):  # iterate through each team
            if teams[i] + currentSkill <= target:
                teams[i] += currentSkill

                if backtrack(arrayidx + 1):
                    return True

                teams[i] -= currentSkill
        return False

    return backtrack(0)


# print( canFormBalancedTeams([4,3,2,3,5,2,1], 4))
# print(canFormBalancedTeams([2, 1, 3, 4, 2], 3))
print(canFormBalancedTeams([2, 1, 3,4,5], 3))
print(canFormBalancedTeams([], 0))

s1 = set([1,2,3,4,5,5])
s2 = set([3,4,5,6,7,8])
print (s1 | s2)
print (s1 & s2)
print (s1 ^ s2)