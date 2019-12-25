# title: binary-tree-right-side-view
# detail: https://leetcode.com/submissions/detail/284306411/
# datetime: Sat Dec  7 19:38:46 2019
# runtime: 40 ms
# memory: 12.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        nodes = []
        if root:
            nodes.append(root)
        while nodes:
            res.append(nodes[-1].val)
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes
        return res