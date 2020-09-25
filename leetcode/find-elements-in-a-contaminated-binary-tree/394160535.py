# title: find-elements-in-a-contaminated-binary-tree
# detail: https://leetcode.com/submissions/detail/394160535/
# datetime: Fri Sep 11 18:55:09 2020
# runtime: 84 ms
# memory: 18.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.values = {0}
        root.val = 0
        self.recover(root.left, 1)
        self.recover(root.right, 2)
        
    def recover(self, root, val):
        if root is None:
            return
        root.val = val
        self.values.add(val)
        self.recover(root.left, 2 * val + 1)
        self.recover(root.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)