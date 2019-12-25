# title: partition-list
# detail: https://leetcode.com/submissions/detail/146337699/
# datetime: Thu Mar 22 10:51:40 2018
# runtime: 40 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left_part_head = None
        left_part_prev_node = None
        left_part_node = None
        right_part_head = None
        right_part_prev_node = None
        
        node = head
        
        while node:
            if node.val < x:
                if left_part_head is None:
                    left_part_head = node
                    left_part_prev_node = node
                    left_part_node = node
                else:
                    left_part_prev_node.next = node
                    left_part_prev_node = node
                    
            else:
                if right_part_head is None:
                    right_part_head = node
                    right_part_prev_node = node
                else:
                    right_part_prev_node.next = node
                    right_part_prev_node = node
            node = node.next
        if left_part_prev_node:
            left_part_prev_node.next = right_part_head
        if right_part_prev_node:
            right_part_prev_node.next = None
        return left_part_head if left_part_head else right_part_head
                
        