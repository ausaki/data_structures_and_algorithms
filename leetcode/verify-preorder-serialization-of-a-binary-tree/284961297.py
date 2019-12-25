# title: verify-preorder-serialization-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/284961297/
# datetime: Tue Dec 10 14:08:28 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1
        for node in nodes:
            slots -= 1
            if slots < 0:
                break
            if node != '#':
                slots += 2
        return slots == 0
            