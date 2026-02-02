'''
Explore

- if the tree has one node return the value in the node
- if the tree is empty the return 0
- i can assume that the value can be any integer


Brainstorm
-do a recursion through the tree...visit every node
-keep a frequency map of counts per value
-when finished return the maximum value
- o(number of nodes) time complexity, o(number of discrete values) space complexity


Plan:
define get max function
    check for empty node
    check for single node
    create counter
    return dfs(node, (0,0))
define dfs(node)
        define base case if not node return maxtuple
        visit left children
        visit right children


return max(counter.values())

'''
from collections import Counter


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def mostFrequentNumberBT(root: TreeNode) -> int:
    if not root:
        return -1
    if not root.left and not root.right:
        return root.value
    freq = Counter()

    def dfs(root):
        if not root:
            return
        print(root.value)
        freq[root.value] += 1
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    print(freq.values())
    max_count = max(freq.values())
    winners = [k for k, v in freq.items() if v == max_count]
    return winners


root = TreeNode(2)
l1 = TreeNode(2)
r1 = TreeNode(1)
l2 = TreeNode(3)
root.left = l1
root.right = r1
l1.left = l2

print(mostFrequentNumberBT(root))