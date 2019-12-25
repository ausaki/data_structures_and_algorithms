# title: linked-list-cycle
# detail: https://leetcode.com/submissions/detail/193078198/
# datetime: Mon Dec  3 13:36:44 2018
# runtime: 48 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_set = set()
        while head:
            node_set.add(head)
            if head.next in node_set:
                return True
            head = head.next
        return False
        