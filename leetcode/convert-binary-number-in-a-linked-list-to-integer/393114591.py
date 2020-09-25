# title: convert-binary-number-in-a-linked-list-to-integer
# detail: https://leetcode.com/submissions/detail/393114591/
# datetime: Wed Sep  9 12:27:34 2020
# runtime: 24 ms
# memory: 14 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        while head:
            n <<= 1
            n |= head.val
            head = head.next
        return n