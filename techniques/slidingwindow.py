'''

Sliding window approach O(n)
'''


from typing import List

def largest_sliding_window(k: int, arr: List[int]) -> int:
    left = cur = ans = 0
    for right in range(len(arr)):
        cur += arr[right]
        while cur > k:
            cur -= arr[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans
print (largest_sliding_window(6, [2,4,5,6,7,4,1,1]))




def longest_substring_with_a_zero(arr):
    left = cur= ans= 0
    for right in range (len(arr)):
        if arr[right] == 0:
            cur += 1
            while cur > 1:
                if arr[left] == 0:
                    cur -= 1
                left += 1

        ans = max(ans, right-left + 1)
    return ans
print(longest_substring_with_a_zero([1,1,0,0,0,0,1,1,0,0,1,0]))


def num_seq_with_product_lessthan_k(arr, k):
    if k <1:
        return 0
    left = ans = 0
    curr = 1
    for right in range(len(arr)):
        curr = curr * arr[right]
        while curr >= k:
            curr //= arr[left]
            left += 1
        ans += right - left + 1

    return ans

print (num_seq_with_product_lessthan_k([1,4,3,9,6,4], 12))