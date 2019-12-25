# title: insertion-sort-list
# detail: https://leetcode.com/submissions/detail/284124533/
# datetime: Fri Dec  6 19:49:09 2019
# runtime: 244 ms
# memory: 14.5 MB

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
            print(curr.val)
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
            