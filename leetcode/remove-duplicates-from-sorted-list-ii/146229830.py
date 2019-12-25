# title: remove-duplicates-from-sorted-list-ii
# detail: https://leetcode.com/submissions/detail/146229830/
# datetime: Wed Mar 21 17:41:57 2018
# runtime: 49 ms
# memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        node = node = head.next
        new_head = None
        new_node = None
        count = 1
        
        if node is None:
            return head
        
        prev_node = head
        prev_val = head.val
        
        while node:
            if node.val == prev_val:
                count += 1
            else:
                if count == 1:
                    if new_head is None:
                        new_head = prev_node
                        new_node = prev_node
                    else:
                        new_node.next = prev_node
                        new_node = prev_node
                
                prev_val = node.val
                count = 1
            
            prev_node = node
            node = node.next
        
        if count == 1:
            if new_head is None:
                new_head = prev_node
                new_node = prev_node
            else:
                new_node.next = prev_node
                new_node = prev_node
        if new_node:
            new_node.next = None
            
        return new_head
        