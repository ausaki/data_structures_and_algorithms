# title: insertion-sort-list
# detail: https://leetcode.com/submissions/detail/284124837/
# datetime: Fri Dec  6 19:53:06 2019
# runtime: 236 ms
# memory: 14.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        node = ListNode(-(1 << 31))
        head, node.next = node, head
        prev = head
        curr = prev.next
        while curr:
            while curr and curr.val >= prev.val:
                prev = curr
                curr = curr.next
            if curr is None:
                break
            prev.next = curr.next
            node = head
            while node.next and curr.val > node.next.val:
                node = node.next
            node.next, curr.next = curr, node.next
            curr = prev.next
        return head.next            
            