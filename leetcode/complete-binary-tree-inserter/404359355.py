# title: complete-binary-tree-inserter
# detail: https://leetcode.com/submissions/detail/404359355/
# datetime: Sun Oct  4 20:09:02 2020
# runtime: 60 ms
# memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        row = [root]
        while True:
            new = []
            f = False
            for i, node in enumerate(row):
                if node.left:
                    new.append(node.left)
                else:
                    f = True
                    break
                if node.right:
                    new.append(node.right)
                else:
                    f = True
                    break
            if f:
                self.i = i
                break
            row = new
        self.last_row = row

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        parent = self.last_row[self.i]
        if parent.left is None:
            parent.left = node
            return parent.val
        if parent.right is None:
            parent.right = node
            self.i += 1
            if self.i == len(self.last_row):
                row = []
                for node in self.last_row:
                    row.append(node.left)
                    row.append(node.right)
                self.last_row = row
                self.i = 0
            return parent.val
        
    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()