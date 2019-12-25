# title: most-frequent-subtree-sum
# detail: https://leetcode.com/submissions/detail/286834740/
# datetime: Wed Dec 18 15:50:19 2019
# runtime: 48 ms
# memory: 16.3 MB

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
        if root is None:
            return []
        counter = collections.Counter()
        calc(root)
        max_cnt = max(counter.values())
        return [s for s, c  in counter.items() if c == max_cnt]
