# title: odd-even-linked-list
# detail: https://leetcode.com/submissions/detail/284951048/
# datetime: Tue Dec 10 13:23:27 2019
# runtime: 44 ms
# memory: 14.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = odd_head = head
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return odd_head
