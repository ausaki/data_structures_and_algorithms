# title: path-sum
# detail: https://leetcode.com/submissions/detail/148085758/
# datetime: Mon Apr  2 11:27:42 2018
# runtime: 62 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum, level=0):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return root.val == sum
        elif root.left is not None and root.right is not None:
                return self.hasPathSum(root.left, sum - root.val, level + 1) or self.hasPathSum(root.right, sum - root.val, level + 1)
        elif root.left is not None:
            return self.hasPathSum(root.left, sum - root.val, level + 1)
        else:
            return self.hasPathSum(root.right, sum - root.val, level + 1)
        