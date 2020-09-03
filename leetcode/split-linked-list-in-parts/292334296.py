# title: split-linked-list-in-parts
# detail: https://leetcode.com/submissions/detail/292334296/
# datetime: Wed Jan  8 19:17:32 2020
# runtime: 32 ms
# memory: 12.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = [None] * k
        N = 0
        curr = root
        while curr:
            N += 1
            curr = curr.next
        n, m = divmod(N, k)
        curr = root
        prev = ListNode(0)
        i = 0
        j = 0
        while curr and j < k:
            if j <= m:
                r = i % (n + 1) 
                if r == 0:
                    prev.next = None
                    res[j] = curr
                    j += 1
            else:
                r = (i - m * (n + 1)) % n 
                if r == 0:
                    prev.next = None
                    res[j] = curr
                    j += 1
            prev = curr
            curr = curr.next
            i += 1
        return res