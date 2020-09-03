# title: count-good-nodes-in-binary-tree
# detail: https://leetcode.com/submissions/detail/382202628/
# datetime: Mon Aug 17 21:01:41 2020
# runtime: 236 ms
# memory: 32.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def travel(root, max_val):
            if root is None:
                return 0
            cnt = 0
            if root.val >= max_val:
                cnt += 1
                max_val = root.val
            cnt += travel(root.left, max_val) + travel(root.right, max_val)
            return cnt
        return travel(root, -1e5)