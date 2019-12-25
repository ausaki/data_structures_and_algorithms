# title: serialize-and-deserialize-binary-tree
# detail: https://leetcode.com/submissions/detail/286051727/
# datetime: Sun Dec 15 12:24:06 2019
# runtime: 100 ms
# memory: 17.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = ','
    NULL = 'x'
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        data = [str(root.val)]
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                data.append(str(node.left.val))
            else:
                data.append(self.NULL)
            if node.right:
                queue.append(node.right)
                data.append(str(node.right.val))
            else:
                data.append(self.NULL)
        while data and data[-1] == self.NULL:
            data.pop()
        return self.SEP.join(data)
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        print(data)
        if not data: return None
        data = collections.deque(data.split(self.SEP))
        root = TreeNode(int(data.popleft()))
        queue = collections.deque()
        queue.append(root)
        while data and queue:
            node = queue.popleft()
            leftval = data.popleft() if data else self.NULL
            rightval = data.popleft() if data else self.NULL
            if leftval != self.NULL:
                node.left = TreeNode(int(leftval))
                queue.append(node.left)
            if rightval != self.NULL:
                node.right = TreeNode(int(rightval))
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))