# title: add-two-numbers-ii
# detail: https://leetcode.com/submissions/detail/285886891/
# datetime: Sat Dec 14 22:19:31 2019
# runtime: 68 ms
# memory: 12.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(node):
            prev, curr = None, node
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        l3 = ListNode(0)
        i = l1
        j = l2
        k = l3
        sup = 0
        while i or j:
            sup, v = divmod(sup + (i.val if i else 0) + (j.val if j else 0), 10)
            if i: i = i.next
            if j: j = j.next
            node = ListNode(v)
            k.next = node
            k = k.next
        if sup:
            k.next = ListNode(sup)
        l3 = reverse(l3.next)
        return l3