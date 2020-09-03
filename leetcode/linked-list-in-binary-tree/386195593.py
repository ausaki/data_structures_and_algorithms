# title: linked-list-in-binary-tree
# detail: https://leetcode.com/submissions/detail/386195593/
# datetime: Tue Aug 25 23:15:11 2020
# runtime: 196 ms
# memory: 15.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def match(root, head):
            if head is None:
                return True
            if root is None:
                return False
            if root.val == head.val:
                return match(root.left, head.next) or match(root.right, head.next)
            return False
        
        def travel(root):
            if root is None:
                return False
            return match(root, head) or travel(root.left) or travel(root.right)
        
        return travel(root)
                