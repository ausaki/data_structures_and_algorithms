# title: verify-preorder-serialization-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/284957897/
# datetime: Tue Dec 10 13:53:47 2019
# runtime: 32 ms
# memory: 12.9 MB

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        def validate(i):
            if i >= len(nodes):
                return -1
            if nodes[i] == '#':
                return i + 1
            i = validate(i + 1)
            if i == -1:
                return i
            return validate(i)
        i = validate(0)
        return i == len(nodes)
            