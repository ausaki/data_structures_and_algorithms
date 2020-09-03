# title: split-linked-list-in-parts
# detail: https://leetcode.com/submissions/detail/292332787/
# datetime: Wed Jan  8 19:03:36 2020
# runtime: 28 ms
# memory: 13 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = []
        N = 0
        curr = root
        while curr:
            N += 1
            curr = curr.next
        n, m = divmod(N, k)
        curr = root
        prev = None
        i = 0
        j = 0
        while curr:
            if j <= m:
                if i % (n + 1) == 0:
                    if prev:
                        prev.next = None
                    res.append(curr)
                    j += 1
            else:
                if (i - m * (n + 1)) % n == 0:
                    prev.next = None
                    res.append(curr)
            prev = curr
            curr = curr.next
            i += 1
        if len(res) < k:
            res += [None] * (k - len(res))
        return res