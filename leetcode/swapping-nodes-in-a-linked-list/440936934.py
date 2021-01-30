# title: swapping-nodes-in-a-linked-list
# detail: https://leetcode.com/submissions/detail/440936934/
# datetime: Sun Jan 10 10:43:26 2021
# runtime: 1356 ms
# memory: 48.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        l, r = head, head
        for i in range(k - 1):
            r = r.next
        s = r
        while r.next:
            l = l.next
            r = r.next
        t = l
        s.val, t.val = t.val, s.val
        return head