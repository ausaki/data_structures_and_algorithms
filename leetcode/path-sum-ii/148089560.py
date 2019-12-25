# title: path-sum-ii
# detail: https://leetcode.com/submissions/detail/148089560/
# datetime: Mon Apr  2 11:50:26 2018
# runtime: 99 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _pathSum(self, root, sum):
        if root is None:
            return 
        
        self._path.append(root.val)
        if root.left is None and root.right is None:
            if root.val == sum:
                self._result.append(self._path[:])
        elif root.left is not None and root.right is not None:
            self._pathSum(root.left, sum - root.val) or self._pathSum(root.right, sum - root.val)
        elif root.left is not None:
            self._pathSum(root.left, sum - root.val)
        else:
            self._pathSum(root.right, sum - root.val)
        self._path.pop()
        
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self._result = []
        self._path = []
        self._pathSum(root, sum)
        return self._result
        