from typing import List
from collections import defaultdict


def prioritize_sightings(sightings: List[int]) -> List[int]:
    if not sightings:
        return []

    countMap = defaultdict(int)
    for species in sightings:
        countMap[species] +=  1

    retarr = sorted(sightings, key=lambda x: (countMap[x], -x))
    print(retarr)
    return retarr


# print((prioritize_sightings([4, 4, 2, 2, 2, 7]) == [7, 4, 4, 2, 2, 2]) == True)

# print((prioritize_sightings([1, 1, 3, 3, 5, 5]) == [5, 5, 3, 3, 1, 1]) == True)

#print((prioritize_sightings([1, 3, 2, 3, 2, 2, 3]) == [1, 3, 3, 3, 2, 2, 2, ]) == True)


myarr = [1,3,5,7,9]
print(sorted(myarr, key= lambda x: (print(x), x)))