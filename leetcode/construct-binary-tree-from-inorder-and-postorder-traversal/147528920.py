# title: construct-binary-tree-from-inorder-and-postorder-traversal
# detail: https://leetcode.com/submissions/detail/147528920/
# datetime: Thu Mar 29 17:54:16 2018
# runtime: 312 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        inorder: left parent right
        postorder: left right parent
        """
        if not inorder or not postorder:
            return None
        parent_val = postorder.pop()
        index = inorder.index(parent_val)
        parent_node = TreeNode(parent_val)
        parent_node.left = self.buildTree(inorder[:index], postorder[:index])
        parent_node.right = self.buildTree(inorder[index + 1:], postorder[index:])
        return parent_node
        
        