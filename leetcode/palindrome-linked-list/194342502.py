# title: palindrome-linked-list
# detail: https://leetcode.com/submissions/detail/194342502/
# datetime: Mon Dec 10 15:36:17 2018
# runtime: 116 ms
# memory: 26.7 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tail = prev
        while tail and head and tail.val == head.val:
            tail = tail.next
            head = head.next
        return tail is None
        
        