# title: range-sum-query---mutable
# detail: https://leetcode.com/submissions/detail/282465395/
# datetime: Fri Nov 29 19:18:30 2019
# runtime: 248 ms
# memory: 24.5 MB

class Node:
    def __init__(self):
        self.val = 0
        self.range = [-1, -1]
        self.left = None
        self.right = None
    def __str__(self):
        return '{}, {}'.format(self.val, self.range)
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.root = None
        self._buildtree(nums)
        
    def _buildtree(self, nums):
        def _dfs(i, j):
            node = Node()
            node.range[0] = i
            node.range[1] = j
            if i == j:
                node.left = node.right = None
                node.val = nums[i]
            else:
                m = (i + j) // 2
                node.left = _dfs(i, m)
                node.right = _dfs(m + 1, j)
                node.val = node.left.val + node.right.val
            return node
        if self.size == 0:
            return None
        self.root = _dfs(0, len(nums) - 1)
    
    def update(self, i: int, val: int) -> None:
        def _update(node):
            if node.left is None:
                node.val = val
                return val
            if i <= node.left.range[1]:
                node.val = _update(node.left) + node.right.val
            else:
                node.val = _update(node.right) + node.left.val
            return node.val
        if i < 0 or i >= self.size:
            return
        _update(self.root)
        

    def sumRange(self, i: int, j: int) -> int:
        def _sum(node, i, j):
            if [i, j] == node.range:
                return node.val
            if i > node.left.range[1]:
                return _sum(node.right, i, j)
            if j < node.right.range[0]:
                return _sum(node.left, i, j)
            return _sum(node.left, i, node.left.range[1]) + _sum(node.right, node.right.range[0], j)
        if i > j or i < 0 or i >= self.size or j >= self.size:
            return -1
        return _sum(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)