# title: all-nodes-distance-k-in-binary-tree
# detail: https://leetcode.com/submissions/detail/407305503/
# datetime: Sun Oct 11 17:42:11 2020
# runtime: 36 ms
# memory: 14.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        def find(root):
            if root is None:
                return False
            if root is target:
                return True
            if find(root.left):
                root.left.parent, root.left = root, None
                return True
            if find(root.right):
                root.right.parent, root.right = root, None
                return True
            return False
        def dfs(root, h):
            if root is None:
                return
            if h == 0:
                result.append(root.val)
                return
            dfs(root.left, h - 1)
            dfs(root.right, h - 1)
        find(root)
        result = []
        while K >= 0 and target:
            dfs(target, K)
            target = getattr(target, 'parent', None)
            K -= 1
        return result
            