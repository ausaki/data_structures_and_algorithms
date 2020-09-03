# title: linked-list-in-binary-tree
# detail: https://leetcode.com/submissions/detail/386211322/
# datetime: Tue Aug 25 23:56:44 2020
# runtime: 84 ms
# memory: 15.9 MB

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
        table = [0]
        arr = [head.val]
        head = head.next
        while head:
            i = table[-1]
            val = head.val
            while i and val != arr[i]:
                i = table[i - 1]
            if val == arr[i]:
                i += 1 
            table.append(i)
            arr.append(head.val)
            head = head.next
        
        def match(root, i):
            if i == len(arr):
                return True
            if root is None:
                return False
            while i and root.val != arr[i]:
                i = table[i - 1]
            if root.val == arr[i]:
                i += 1
            return match(root.left, i) or match(root.right, i)
        
        return match(root, 0)
                