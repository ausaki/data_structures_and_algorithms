# title: linked-list-random-node
# detail: https://leetcode.com/submissions/detail/285257658/
# datetime: Wed Dec 11 21:48:57 2019
# runtime: 76 ms
# memory: 15.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.size = 0
        while head:
            self.size += 1
            head = head.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        k = random.randrange(self.size)
        i = 0
        head = self.head
        while i < k:
            head = head.next
            i += 1
        return head.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()