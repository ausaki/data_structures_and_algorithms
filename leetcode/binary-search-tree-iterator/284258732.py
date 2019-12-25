# title: binary-search-tree-iterator
# detail: https://leetcode.com/submissions/detail/284258732/
# datetime: Sat Dec  7 13:08:53 2019
# runtime: 72 ms
# memory: 20 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.initstack()
        
    def initstack(self):
        if self.root is None:
            return
        self.stack.append(self.root)
        while self.stack[-1].left:
            self.stack.append(self.stack[-1].left)
            
    def fillstack(self, node):
        if node.right is None:
            return
        self.stack.append(node.right)
        while self.stack[-1].left:
            self.stack.append(self.stack[-1].left)
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.fillstack(node)
        return node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()