# title: reverse-linked-list-ii
# detail: https://leetcode.com/submissions/detail/147030145/
# datetime: Mon Mar 26 17:32:21 2018
# runtime: 36 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev = None
        curr = None
        next_ = None
        m_left_node = None
        m_node = None
        
        i = 1
        
        
        curr = head
        while curr and i < m:
            m_left_node = curr
            curr = curr.next
            i += 1
        m_node = curr
        if curr is None:
            return curr
        
        while curr and i <= n:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            i += 1
        
        if m_left_node:
            m_left_node.next = prev
        m_node.next = curr
        
        if m == 1 :
            head = prev
        return head
        