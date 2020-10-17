# title: linked-list-components
# detail: https://leetcode.com/submissions/detail/409307036/
# datetime: Fri Oct 16 12:01:47 2020
# runtime: 108 ms
# memory: 18.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g = dict.fromkeys(G, -1)
        i = 0
        while head:
            if head.val not in g:
                i += 1
            else:
                g[head.val] = i
            head = head.next
        return len(set(g.values()))