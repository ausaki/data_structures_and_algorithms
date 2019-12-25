# title: unique-binary-search-trees-ii
# detail: https://leetcode.com/submissions/detail/147199063/
# datetime: Tue Mar 27 16:59:18 2018
# runtime: 104 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def copyTree(self, root):
        if root is None:
            return None
        parent = TreeNode(root.val)
        parent.left = self.copyTree(root.left)
        parent.right = self.copyTree(root.right)
        return parent
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # Dynamic Programing
        # T(n) = C(n, T(n - 1))
        if n == 0:
            return []
        
        if n == 1:
            return [TreeNode(1)]
        new_trees = []
        trees = self.generateTrees(n - 1)
        node_n = TreeNode(n)
        
        # node_n as the new root node
        # node_n.left = old_root
        for tree in trees:
            node_n = TreeNode(n)
            node_n.left = tree
            new_trees.append(node_n)
        
        for tree in trees:
            current_node = tree
            while current_node:
                root = self.copyTree(tree)
                node = root
                while node.val != current_node.val:
                    node = node.right
                node_n = TreeNode(n)
                right_node = node.right
                node.right = node_n
                node_n.left = right_node
                new_trees.append(root)
                    
                current_node = right_node
                
        return new_trees
        
        