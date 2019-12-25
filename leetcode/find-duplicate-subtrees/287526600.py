# title: find-duplicate-subtrees
# detail: https://leetcode.com/submissions/detail/287526600/
# datetime: Sat Dec 21 21:10:28 2019
# runtime: 68 ms
# memory: 21.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def encode(root):
            if root is None:
                return '#'
            s = '{},{},{}'.format(root.val, encode(root.left), encode(root.right))
            # print(s)
            if s not in seen:
                seen[s] = 1
            elif seen[s] == 1:
                seen[s] += 1
                res.append(root)
            return s
        seen = {}
        res = []
        encode(root)
        return res