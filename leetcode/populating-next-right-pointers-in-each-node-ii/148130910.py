# title: populating-next-right-pointers-in-each-node-ii
# detail: https://leetcode.com/submissions/detail/148130910/
# datetime: Mon Apr  2 17:07:47 2018
# runtime: 98 ms
# memory: N/A

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        
        qeuue = [(root, 0)]
        level = -1
        prev = None
        
        while qeuue:
            node, level_ = qeuue.pop(0)
            if level_ == level:
                prev.next = node
                prev = node
            else:
                level = level_
                if prev:
                    prev.next = None
                prev = node
            if node.left:
                qeuue.append((node.left, level_ + 1))
            if node.right:
                qeuue.append((node.right, level_ + 1))
        prev.next = None