# title: most-frequent-subtree-sum
# detail: https://leetcode.com/submissions/detail/286833494/
# datetime: Wed Dec 18 15:43:59 2019
# runtime: 52 ms
# memory: 16.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def calc(root):
            if root is None:
                return 0
            val = root.val + calc(root.left) + calc(root.right)
            counter[val] += 1
            return val
        counter = collections.Counter()
        calc(root)
        # print(counter)
        items = sorted(counter.items(), key=lambda item: item[1])
        if not items:
            return []
        res = [items[-1][0]]
        for i in range(len(items) - 2, -1, -1):
            if items[i][1] == items[i + 1][1]:
                res.append(items[i][0])
            else:
                break
        return res