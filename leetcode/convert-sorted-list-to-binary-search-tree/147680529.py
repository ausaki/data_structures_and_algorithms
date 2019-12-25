# title: convert-sorted-list-to-binary-search-tree
# detail: https://leetcode.com/submissions/detail/147680529/
# datetime: Fri Mar 30 18:05:43 2018
# runtime: 284 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head, tail=None):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # print head.val if head else head, tail.val if tail else tail
        if head == tail:
            return None
        
        slow = head
        fast = head.next
        
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        parent = TreeNode(slow.val)
        parent.left = self.sortedListToBST(head, slow)
        parent.right = self.sortedListToBST(slow.next, tail)
        return parent
        
        