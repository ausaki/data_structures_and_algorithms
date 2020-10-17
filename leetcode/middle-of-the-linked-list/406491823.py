# title: middle-of-the-linked-list
# detail: https://leetcode.com/submissions/detail/406491823/
# datetime: Fri Oct  9 15:57:44 2020
# runtime: 16 ms
# memory: 14.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow