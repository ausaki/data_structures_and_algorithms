# title: convert-sorted-array-to-binary-search-tree
# detail: https://leetcode.com/submissions/detail/147676303/
# datetime: Fri Mar 30 17:07:33 2018
# runtime: 87 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST_(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        parent = TreeNode(nums[mid])
        parent.left = self.sortedArrayToBST_(nums, start, mid - 1)
        parent.right = self.sortedArrayToBST_(nums, mid + 1, end)
        return parent
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBST_(nums, 0, len(nums) - 1)