# title: sort-list
# detail: https://leetcode.com/submissions/detail/284131952/
# datetime: Fri Dec  6 21:16:46 2019
# runtime: 180 ms
# memory: 19.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def quicksort(node, size):
            pass
        def mergesort(node):
            if node is None or node.next is None:
                return node
            slow = node
            fast = slow.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            new_node = slow.next
            slow.next = None
            left = mergesort(node)
            right = mergesort(new_node)
            
            # merge
            i = left
            j = right
            while i and j:
                prev = None
                while i and i.val <= j.val:
                    prev = i
                    i = i.next
                if prev:
                    prev.next = j
                if i is None:
                    break
                prev = None
                while j and j.val <= i.val:
                    prev = j
                    j = j.next
                if prev:
                    prev.next = i
            return left if left.val <= right.val else right
        
        return mergesort(head)