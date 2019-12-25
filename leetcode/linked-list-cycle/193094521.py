# title: linked-list-cycle
# detail: https://leetcode.com/submissions/detail/193094521/
# datetime: Mon Dec  3 14:59:51 2018
# runtime: 44 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        prev = None
        next = head
        while next:
            tmp = next.next
            next.next = prev
            prev = next
            next = tmp
        return head == prev
        