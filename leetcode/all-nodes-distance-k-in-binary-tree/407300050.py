# title: all-nodes-distance-k-in-binary-tree
# detail: https://leetcode.com/submissions/detail/407300050/
# datetime: Sun Oct 11 17:17:04 2020
# runtime: 36 ms
# memory: 14.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        result = []
        target_h = -1
        def visit(root, h, H):
            if root is None:
                return -1
            if h == H:
                result.append(root.val)
                return -1
            if root is target:
                H = h + K
                if h == H:
                    result.append(root.val)
            t = visit(root.left, h + 1, H)
            if t != -1:
                if K - t + h == 0:
                    result.append(root.val)
                else:
                    visit(root.right, h + 1, 2 * h + K - t)
                return t
            t = visit(root.right, h + 1, H)
            if t != -1:
                if K - t + h == 0:
                    result.append(root.val)
                else:
                    visit(root.left, h + 1, 2 * h + K - t)
                return t
            return h if root is target else -1
        visit(root, 0, -1)
        return result
            