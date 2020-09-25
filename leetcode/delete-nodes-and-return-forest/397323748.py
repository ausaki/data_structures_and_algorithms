# title: delete-nodes-and-return-forest
# detail: https://leetcode.com/submissions/detail/397323748/
# datetime: Fri Sep 18 12:46:51 2020
# runtime: 56 ms
# memory: 14.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)
        def delete(root, isroot):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = delete(root.left, True)
                root.right = delete(root.right, True)
                return None
            if isroot:
                result.append(root)
            root.left = delete(root.left, False)
            root.right = delete(root.right, False)
            return root
        
        delete(root, True)
        return result