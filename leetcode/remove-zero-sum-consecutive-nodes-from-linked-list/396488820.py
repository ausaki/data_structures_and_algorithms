# title: remove-zero-sum-consecutive-nodes-from-linked-list
# detail: https://leetcode.com/submissions/detail/396488820/
# datetime: Wed Sep 16 15:44:34 2020
# runtime: 60 ms
# memory: 14.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        sums = {0: dummy}
        s = 0
        while head:
            s += head.val
            if s in sums:
                node = sums[s]
                while node.next is not head:
                    s += node.next.val
                    sums.pop(s)
                    node.next = node.next.next
                node.next = head.next
                s += head.val
            else:
                sums[s] = head
            head = head.next
        return sums[0].next