# title: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# detail: https://leetcode.com/submissions/detail/376936900/
# datetime: Thu Aug  6 19:22:31 2020
# runtime: 9400 ms
# memory: 90 MB

class SegmentTreeNode:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.min = None
        self.min_indices = []

class SegmentTree:

    def __init__(self, seq) -> None:
        self._seq = seq
        self._root = self._build_tree(0, len(self._seq) - 1)
    
    def _build_tree(self, start, end):
        if start > end:
            return None
        if start == end:
            root = SegmentTreeNode(start, end)
            root.min = self._seq[start]
            root.min_indices = [start]
            return root
        mid = (start + end) // 2
        left_node = self._build_tree(start, mid)
        right_node = self._build_tree(mid + 1, end)
        root = SegmentTreeNode(start, end)
        root.left = left_node
        root.right = right_node
        if left_node.min == right_node.min:
            root.min = left_node.min
            root.min_indices = left_node.min_indices + right_node.min_indices
        elif left_node.min < right_node.min:
            root.min = left_node.min
            root.min_indices = left_node.min_indices
        else:
            root.min = right_node.min
            root.min_indices = right_node.min_indices
        return root

    def _query(self, root: SegmentTreeNode, start, end):
        if start == root.start and end == root.end:
            return root.min, root.min_indices
        left = root.left
        right = root.right
        if start > left.end:
            return self._query(right, start, end)
        if end < right.start:
            return self._query(left, start, end)
        l_min, l_indices = self._query(left, start, left.end)
        r_min, r_indices = self._query(right, right.start, end)
        if l_min == r_min:
            return l_min, l_indices + r_indices
        if l_min < r_min:
            return l_min, l_indices
        return  r_min, r_indices

    def query(self, start, end):
        return self._query(self._root, start, end)
    
    
    
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        segment_tree = SegmentTree(target)
        
        queue = collections.deque()
        queue.append((0, len(target) -1, 0))
        result = 0
        while queue:
            left, right, level = queue.popleft()
            if left > right:
                continue
            m, indices = segment_tree.query(left, right)
            result += m - level
            level = m
            for i in indices:
                queue.append((left, i - 1, level))
                left = i + 1
            queue.append((left, right, level))
        return result
        
        return count(0, len(target) - 1, 0)
            