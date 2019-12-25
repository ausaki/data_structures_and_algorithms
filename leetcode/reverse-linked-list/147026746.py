# title: reverse-linked-list
# detail: https://leetcode.com/submissions/detail/147026746/
# datetime: Mon Mar 26 16:58:12 2018
# runtime: 42 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = None
        next_ = None
        
        curr = head
        
        if curr is None:
            return curr
        
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        return prev
            
        