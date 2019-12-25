# title: binary-tree-paths
# detail: https://leetcode.com/submissions/detail/195723486/
# datetime: Tue Dec 18 15:39:43 2018
# runtime: 24 ms
# memory: 7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        paths = []
        if root.left:
            left_paths = self.binaryTreePaths(root.left)
            for p in left_paths:
                paths.append('{}->{}'.format(root.val, p))
        if root.right:
            right_paths = self.binaryTreePaths(root.right)
            for p in right_paths:
                paths.append('{}->{}'.format(root.val, p))
        return paths
        