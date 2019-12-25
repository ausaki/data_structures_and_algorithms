# title: print-binary-tree
# detail: https://leetcode.com/submissions/detail/287500245/
# datetime: Sat Dec 21 16:34:54 2019
# runtime: 32 ms
# memory: 12.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def count(root):
            if root is None:
                return 0, 0
            h1, w1 = count(root.left)
            h2, w2 = count(root.right)
            return max(h1, h2) + 1, max(w1, w2) * 2 + 1
        def _print(node, i, j):
            if node is None:
                return
            table[i][j] = str(node.val)
            k = w // (2 ** (i + 2))
            _print(node.left, i + 1, j - k - 1)
            _print(node.right, i + 1, j + k + 1)
        h, w = count(root)
        table = [[''] * w for i in range(h)]
        _print(root, 0, w // 2)
        return table