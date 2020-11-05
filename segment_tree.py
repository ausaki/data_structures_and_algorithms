class SegmentTreeNode:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.left :'SegmentTreeNode' = None
        self.right :'SegmentTreeNode' = None
        self.val = None

class SegmentTree:

    def __init__(self, seq) -> None:
        self._seq = seq
        self._root = self._build_tree(0, len(self._seq) - 1)
    
    def _build_tree(self, start, end):
        if start > end:
            return None
        if start == end:
            root = SegmentTreeNode(start, end)
            root.val = self._seq[start]
            return root
        mid = (start + end) // 2
        left_node = self._build_tree(start, mid)
        right_node = self._build_tree(mid + 1, end)
        root = SegmentTreeNode(start, end)
        root.left = left_node
        root.right = right_node
        root.val = min(root.left.val, root.right.val)
        return root

    def _query(self, root: SegmentTreeNode, start, end):
        if start == root.start and end == root.end:
            return root.val
        left = root.left
        right = root.right
        if start > left.end:
            return self._query(right, start, end)
        if end < right.start:
            return self._query(left, start, end)
        lv = self._query(left, start, left.end)
        rv = self._query(right, right.start, end)
        return min(lv, rv)

    def query(self, start, end):
        return self._query(self._root, start, end)
    
    def _update(self, root: SegmentTreeNode, i, val):
        if root.start == root.end == i:
            root.val = val
            return
        l, r = root.left, root.right
        if i <= l.end:
            self._update(l, i, val)
        else:
            self._update(r, i, val)
        root.val = min(root.left.val, root.right.val)

    def update(self, i, val):
        self._update(self._root, i, val)

class ArrayVirtualNode:
    def __init__(self, index, start, end) -> None:
        self.index :int = index
        self.start :int = start
        self.end :int = end
        self.mid = (start + end) // 2
        self.left_index = 2 * index + 1
        self.right_index = 2 * index + 2
    
    @property
    def left(self) -> 'ArrayVirtualNode':
        return ArrayVirtualNode(2 * self.index + 1, self.start, (self.start + self.end) // 2)
    
    @property
    def right(self) -> 'ArrayVirtualNode':
        return ArrayVirtualNode(2 * self.index + 2, (self.start + self.end) // 2 + 1, self.end)

class SegmentTreeWithArray:

    def __init__(self, arr) -> None:
        self.size = len(arr)
        self.tree = [0] * (4 * self.size)
        self.arr = arr
        self.root = ArrayVirtualNode(0, 0, self.size - 1)
        self._build_tree(self.root)
        del self.arr

    def _build_tree(self, root: ArrayVirtualNode):
        if root.start == root.end:
            self.tree[root.index] = self.arr[root.start]
            return 
        l, r = root.left, root.right
        self._build_tree(l)
        self._build_tree(r)
        self.tree[root.index] = min(self.tree[l.index], self.tree[r.index])

    def _query(self, root: ArrayVirtualNode, start, end):
        if root.start == start and root.end == end:
            return self.tree[root.index]
        l, r = root.left, root.right
        if start > l.end:
            return self._query(r, start, end)
        if end <= l.end:
            return self._query(l, start, end)
        lv = self._query(l, start, l.end)
        rv = self._query(r, r.start, end)
        return min(lv, rv)

    def query(self, start, end):
        return self._query(self.root, start, end)

    def _update(self, root: ArrayVirtualNode, i, val):
        if root.start == root.end == i:
            self.tree[root.index] = val
            return
        l, r = root.left, root.right
        if i <= l.end:
            self._update(l, i, val)
        else:
            self._update(r, i, val)
        self.tree[root.index] = min(self.tree[l.index], self.tree[r.index])

    def update(self, i, val):
        self._update(self.root, i, val)

def main():
    seq = list(range(20))
    print('seq', seq)
    seg_tree = SegmentTreeWithArray(seq)
    m = seg_tree.query(0, 6)
    print(m)
    seg_tree.update(5, -1)
    print(seg_tree.query(0, 6))

main()