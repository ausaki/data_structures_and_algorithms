# title: remove-zero-sum-consecutive-nodes-from-linked-list
# detail: https://leetcode.com/submissions/detail/396487208/
# datetime: Wed Sep 16 15:39:31 2020
# runtime: 52 ms
# memory: 14 MB

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
                curr = node.next
                s1 = s
                while curr is not head:
                    s1 += curr.val
                    sums.pop(s1)
                    curr = curr.next
                node.next = head.next
            else:
                sums[s] = head
            head = head.next
        return sums[0].next