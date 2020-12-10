# title: merge-in-between-linked-lists
# detail: https://leetcode.com/submissions/detail/424992419/
# datetime: Sat Nov 28 22:51:47 2020
# runtime: 468 ms
# memory: 20.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_end = list2
        while list2_end.next:
            list2_end = list2_end.next
        curr = list1
        c, d = curr, None
        for i in range(1, b + 2):
            curr = curr.next
            if i == a - 1:
                c = curr
            if i == b + 1:
                d = curr
        c.next = list2
        list2_end.next = d
        return list1