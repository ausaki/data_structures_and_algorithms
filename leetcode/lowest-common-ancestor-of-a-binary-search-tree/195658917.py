# title: lowest-common-ancestor-of-a-binary-search-tree
# detail: https://leetcode.com/submissions/detail/195658917/
# datetime: Tue Dec 18 09:43:06 2018
# runtime: 68 ms
# memory: 19.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        node_p = root
        node_q = root
        print(root)
        prev = None
        while node_p == node_q:
            prev = node_p
            if p.val < node_p.val:
                node_p = node_p.left
            elif p.val == node_p.val:
                return node_p
            else:
                node_p = node_p.right
            if q.val < node_q.val:
                node_q = node_q.left
            elif q.val == node_q.val:
                return node_q
            else:
                node_q = node_q.right
        return prev