# title: linked-list-random-node
# detail: https://leetcode.com/submissions/detail/285387004/
# datetime: Thu Dec 12 11:18:31 2019
# runtime: 88 ms
# memory: 15.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
对于 Follow up 可以参考: https://en.wikipedia.org/wiki/Reservoir_sampling.
'''

import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res = -1
        i = 1
        head = self.head
        while head:
            if random.random() < 1 / i:
                res = head.val
            head = head.next
            i += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()