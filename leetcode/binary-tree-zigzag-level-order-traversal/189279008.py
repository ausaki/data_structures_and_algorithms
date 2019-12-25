# title: binary-tree-zigzag-level-order-traversal
# detail: https://leetcode.com/submissions/detail/189279008/
# datetime: Tue Nov 13 15:15:38 2018
# runtime: 36 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        result = []
        nodes_queue = [root]
        pre_level = 0
        current_level = 1
        root.level = current_level
        
        while nodes_queue:
            node = nodes_queue.pop(0)
            if node.level > current_level:
                current_level = node.level
                
            if current_level > len(result):
                nodes = []
                result.append(nodes)
            else:
                nodes = result[current_level - 1]
            
            if current_level % 2 == 0:
                nodes.insert(0, node.val)
            else:
                nodes.append(node.val)
            
            if node.left is not None:
                node.left.level = current_level + 1
                nodes_queue.append(node.left)
            if node.right is not None:
                node.right.level = current_level + 1
                nodes_queue.append(node.right)
        return result
        
        