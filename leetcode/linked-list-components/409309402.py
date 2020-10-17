# title: linked-list-components
# detail: https://leetcode.com/submissions/detail/409309402/
# datetime: Fri Oct 16 12:08:50 2020
# runtime: 104 ms
# memory: 18.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g = set(G)
        i = 0
        j = -1
        result = 0
        while head:
            if head.val not in g:
                i += 1
            else:
                result += i != j
                j = i
            head = head.next
        return result