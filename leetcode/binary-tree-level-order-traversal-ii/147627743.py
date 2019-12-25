# title: binary-tree-level-order-traversal-ii
# detail: https://leetcode.com/submissions/detail/147627743/
# datetime: Fri Mar 30 11:02:04 2018
# runtime: 49 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        last_level_nodes = [root]
        result = []
        while last_level_nodes:
            result.append([node.val for node in last_level_nodes])
            nodes = []
            for node in last_level_nodes:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            last_level_nodes = nodes
        return list(reversed(result))