# title: symmetric-tree
# detail: https://leetcode.com/submissions/detail/147483040/
# datetime: Thu Mar 29 12:01:36 2018
# runtime: 54 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric_(self, left, right):
        if left and right :
            return left.val == right.val and \
                self.isSymmetric_(left.left, right.right) and \
                self.isSymmetric_(left.right, right.left)
        elif left is None and right is None:
            return True
        else:
            return False
            
        
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetric_(root.left, root.right)
        