# title: convert-binary-number-in-a-linked-list-to-integer
# detail: https://leetcode.com/submissions/detail/393113107/
# datetime: Wed Sep  9 12:24:02 2020
# runtime: 32 ms
# memory: 14.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = []
        while head:
            b.append(head.val)
            head = head.next
        n = 0
        for i, j in enumerate(b):
            n |= j << (len(b) - i - 1)
        return n