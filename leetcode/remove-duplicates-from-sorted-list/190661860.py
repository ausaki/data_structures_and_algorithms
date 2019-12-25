# title: remove-duplicates-from-sorted-list
# detail: https://leetcode.com/submissions/detail/190661860/
# datetime: Tue Nov 20 14:21:17 2018
# runtime: 36 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        val = None
        node = head
        prev = head
        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
                val = node.val
            node = node.next 
        return head