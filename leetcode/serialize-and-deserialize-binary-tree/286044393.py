# title: serialize-and-deserialize-binary-tree
# detail: https://leetcode.com/submissions/detail/286044393/
# datetime: Sun Dec 15 11:55:39 2019
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
            for i in range(len(queue)):
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
        if not data:
            return None
        data = collections.deque(data.split(self.SEP))
        root = TreeNode(int(data.popleft()))
        queue = collections.deque()
        queue.append(root)
        while data and queue:
            for j in range(len(queue)):
                node = queue.popleft()
                left = data.popleft() if data else self.NULL
                right = data.popleft() if data else self.NULL
                if left != self.NULL:
                    left = TreeNode(int(left))
                    queue.append(left)
                    node.left = left
                if right != self.NULL:
                    right = TreeNode(int(right))
                    queue.append(right)
                    node.right = right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))