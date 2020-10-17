# title: complete-binary-tree-inserter
# detail: https://leetcode.com/submissions/detail/404363386/
# datetime: Sun Oct  4 20:26:11 2020
# runtime: 64 ms
# memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = collections.deque()
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node.left is None or node.right is None:
                self.q.append(node)
                
    def insert(self, v: int) -> int:
        node = TreeNode(v)
        self.q.append(node)
        parent = self.q[0]
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.q.popleft()
        return parent.val
        
    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()