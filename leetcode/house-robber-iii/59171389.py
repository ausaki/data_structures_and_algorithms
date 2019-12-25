# title: house-robber-iii
# detail: https://leetcode.com/submissions/detail/59171389/
# datetime: Sat Apr 16 15:20:29 2016
# runtime: 88 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    h = {}
    def maxHere(someNode):

        if someNode in h:
            return h[someNode]
        if not someNode:
            return 0
        poss1 = someNode.val
        poss2 = 0
        if someNode.left:
            poss1 += maxHere(someNode.left.left) + maxHere(someNode.left.right)
            poss2 += maxHere(someNode.left)
        if someNode.right:
            poss1 += maxHere(someNode.right.left) + maxHere(someNode.right.right)
            poss2 += maxHere(someNode.right)
        h[someNode]= max(poss1, poss2)
        return h[someNode]

    return maxHere(root)