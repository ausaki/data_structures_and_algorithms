# title: most-frequent-subtree-sum
# detail: https://leetcode.com/submissions/detail/286833905/
# datetime: Wed Dec 18 15:45:59 2019
# runtime: 52 ms
# memory: 16.9 MB

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
        last_item = items.pop()
        res = [last_item[0]]
        while items and items[-1][1] == last_item[1]:
            res.append(items.pop()[0])
        return res