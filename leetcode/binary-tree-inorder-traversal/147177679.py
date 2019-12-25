# title: binary-tree-inorder-traversal
# detail: https://leetcode.com/submissions/detail/147177679/
# datetime: Tue Mar 27 14:19:28 2018
# runtime: 35 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
    
    def inorderTraversalRecursive(self, root):
        if not root:
            return
        self.inorderTraversalRecursive(root.left)
        self.result.append(root.val)
        self.inorderTraversalRecursive(root.right)
    
    def inorderTraversalIterative(self, root):
        result, stack = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right
        
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # self.inorderTraversalRecursive(root)
        # return self.result
        return self.inorderTraversalIterative(root)
        
        