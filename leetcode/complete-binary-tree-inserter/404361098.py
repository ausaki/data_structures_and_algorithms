# title: complete-binary-tree-inserter
# detail: https://leetcode.com/submissions/detail/404361098/
# datetime: Sun Oct  4 20:16:31 2020
# runtime: 64 ms
# memory: 14.9 MB

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
        new = []
        while True:
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
            row, new = new, []
        self.row = row
        self.last_row = new
        
    def insert(self, v: int) -> int:
        node = TreeNode(v)
        self.last_row.append(node)
        parent = self.row[self.i]
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.i += 1
            if self.i == len(self.row):
                self.row, self.last_row = self.last_row, []
                self.i = 0
        return parent.val
        
    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()