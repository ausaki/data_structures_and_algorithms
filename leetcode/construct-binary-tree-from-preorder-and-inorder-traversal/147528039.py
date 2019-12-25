# title: construct-binary-tree-from-preorder-and-inorder-traversal
# detail: https://leetcode.com/submissions/detail/147528039/
# datetime: Thu Mar 29 17:42:06 2018
# runtime: 343 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        parent_val = preorder[0]
        parent_index = inorder.index(parent_val)
            
        left_inorder = inorder[:parent_index]
        right_inorder  = inorder[parent_index + 1:]
        
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]
            
        parent_node = TreeNode(parent_val)
        parent_node.left = self.buildTree(left_preorder, left_inorder)
        parent_node.right = self.buildTree(right_preorder, right_inorder)
        
        return parent_node
        