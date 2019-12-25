# title: swap-nodes-in-pairs
# detail: https://leetcode.com/submissions/detail/275006431/
# datetime: Fri Nov  1 12:59:24 2019
# runtime: 36 ms
# memory: 13.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        placeholder = ListNode(0)
        placeholder.next = head
        prev = placeholder
        curr = prev.next
        while curr and curr.next:
            next = curr.next
            curr.next, next.next = next.next, curr
            prev.next = next
            prev = curr
            curr = curr.next
        return placeholder.next