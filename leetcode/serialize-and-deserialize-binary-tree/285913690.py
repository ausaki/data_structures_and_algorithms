# title: serialize-and-deserialize-binary-tree
# detail: https://leetcode.com/submissions/detail/285913690/
# datetime: Sun Dec 15 00:56:07 2019
# runtime: 116 ms
# memory: 17.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return 'x'
        s = str(root.val)
        queue = collections.deque()
        queue.append(root)
        while queue:
            tmp = ''
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    tmp += ',' + str(node.left.val)
                else:
                    tmp += ',x'
                if node.right:
                    queue.append(node.right)
                    tmp += ',' + str(node.right.val)
                else:
                    tmp += ',x'
            s += tmp
        s = s.rstrip(',x')
        return s
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def next_item(i):
            if i >= len(data):
                return i, None
            j = data.find(',', i)
            val = ''
            if j == -1:
                j = len(data)
            val = data[i: j]
            i = j + 1
            if val == 'x':
                val = None
            else:
                val = int(val)
            return i, val
        
        N = len(data)
        if N == 0 or data == 'x':
            return None
        i, val = next_item(0)
        root = TreeNode(val)
        queue = collections.deque()
        queue.append(root)
        while i < N and queue:
            for j in range(len(queue)):
                node = queue.popleft()
                i, left = next_item(i)
                i, right = next_item(i)
                if left is not None:
                    left = TreeNode(left)
                    queue.append(left)
                if right is not None:
                    right = TreeNode(right)
                    queue.append(right)
                node.left = left
                node.right = right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))