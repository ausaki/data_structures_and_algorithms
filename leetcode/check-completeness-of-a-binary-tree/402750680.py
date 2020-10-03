# title: check-completeness-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/402750680/
# datetime: Thu Oct  1 01:01:12 2020
# runtime: 32 ms
# memory: 14.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = collections.deque([(root, 1)])
        i = 1
        while q:
            node, k = q.popleft()
            if node.left:
                i += 1
                if 2 * k > i:
                    return False
                q.append((node.left, 2 * k))
            if node.right:
                i += 1
                if 2 * k + 1 > i:
                    return False
                q.append((node.right, 2 * k + 1))
        return True