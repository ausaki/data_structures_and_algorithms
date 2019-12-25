# title: minimum-depth-of-binary-tree
# detail: https://leetcode.com/submissions/detail/189479216/
# datetime: Wed Nov 14 14:13:32 2018
# runtime: 36 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        d1 = self.minDepth(root.left)
        d2 = self.minDepth(root.right)
        if d1 == 0:
            return d2 + 1
        if d2 == 0:
            return d1 + 1
        return min(d1, d2) + 1
    
    def minDepth1(self, root):
        if root is None:
            return 0
        root.depth = 1
        node_queue = [root]
        depth = 1
        while node_queue:
            node = node_queue.pop(0)
            depth = node.depth
            if node.left is None and node.right is None:
                break
            if node.left:
                node.left.depth = depth + 1
                node_queue.append(node.left)
            if node.right:
                node.right.depth = depth + 1
                node_queue.append(node.right)
        return depth