# title: reorder-list
# detail: https://leetcode.com/submissions/detail/283195886/
# datetime: Mon Dec  2 21:12:45 2019
# runtime: 84 ms
# memory: 20.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        tail = prev
        while head != tail and head is not None:
            head.next, tail.next, head, tail = tail, head.next, head.next, tail.next
        
            
        