# title: insertion-sort-list
# detail: https://leetcode.com/submissions/detail/284127589/
# datetime: Fri Dec  6 20:26:06 2019
# runtime: 208 ms
# memory: 14.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(-(1 << 31))
        head, dummy.next = dummy, head
        curr = head
        while curr.next:
            if curr.next.val >= curr.val:
                curr = curr.next
                continue
            node = curr.next
            curr.next = curr.next.next
            prev = head
            while node.val > prev.next.val:
                prev = prev.next
            prev.next, node.next = node, prev.next
        return dummy.next            
            