# title: serialize-and-deserialize-bst
# detail: https://leetcode.com/submissions/detail/285913288/
# datetime: Sun Dec 15 00:53:29 2019
# runtime: 72 ms
# memory: 16.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = ','
    NULL = 'null'
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def _serialize(node):
            if node is None:
                return
            data.append(str(node.val))
            _serialize(node.left)
            _serialize(node.right)
        
        data = []
        _serialize(root)
        return self.SEP.join(data)
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def _deserialize(min_val, max_val):
            if not data or data[0] < min_val or data[0] > max_val:
                return None
            val = data.popleft()
            node = TreeNode(val)
            node.left = _deserialize(min_val, val)
            node.right = _deserialize(val, max_val)
            return node
        
        if not data:
            return None
        data = collections.deque(map(int, data.split(self.SEP)))
        return _deserialize(float('-inf'), float('+inf'))
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))