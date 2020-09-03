# title: balance-a-binary-search-tree
# detail: https://leetcode.com/submissions/detail/385764086/
# datetime: Tue Aug 25 02:16:30 2020
# runtime: 316 ms
# memory: 18.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
        
    def _insert(self, root, val):
        if root is None:
            node = TreeNode(val)
            node.height = 0
            return node
        if val < root.val:
            root.left = self._insert(root.left, val)
            lh = self.height(root.left)
            rh = self.height(root.right)
            if lh - rh > 1:
                if val < root.left.val:
                    root = self.single_rotate_with_left(root)
                else:
                    root = self.double_rotate_with_left(root)
        else:
            root.right = self._insert(root.right, val)
            lh = self.height(root.left)
            rh = self.height(root.right)
            if rh - lh > 1:
                if val > root.right.val:
                    root = self.single_rotate_with_right(root)
                else:
                    root = self.double_rotate_with_right(root)
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        return root
    
    def single_rotate_with_left(self, k2):
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2

        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        return k1

    def single_rotate_with_right(self, k2):
        k1 = k2.right
        k2.right = k1.left
        k1.left = k2

        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        return k1

    def double_rotate_with_left(self, k3):
        k3.left = self.single_rotate_with_right(k3.left)
        return self.single_rotate_with_left(k3)

    def double_rotate_with_right(self, k3):
        k3.right = self.single_rotate_with_left(k3.right)
        return self.single_rotate_with_right(k3)
    
    def height(self, node):
        return node.height if node else -1
    
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
            
        def build(i, j):
            if i > j:
                return
            m = (i + j) // 2
            root = nodes[m]
            root.left = build(i, m - 1)
            root.right = build(m + 1, j)
            return root
        
        nodes = []
        inorder(root)
        return build(0, len(nodes) - 1)
        