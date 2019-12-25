# title: swap-nodes-in-pairs
# detail: https://leetcode.com/submissions/detail/275004388/
# datetime: Fri Nov  1 12:50:35 2019
# runtime: 36 ms
# memory: 13.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        prev = ListNode(0)
        curr = head
        new_head = head.next
        while curr and curr.next:
            n = curr.next
            n.next, curr.next = curr, n.next
            prev.next = n
            prev = curr
            curr = curr.next
        return new_head        
        