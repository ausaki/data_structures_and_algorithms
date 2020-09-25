# title: path-in-zigzag-labelled-binary-tree
# detail: https://leetcode.com/submissions/detail/397399965/
# datetime: Fri Sep 18 16:31:13 2020
# runtime: 28 ms
# memory: 13.8 MB

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        i = 1
        for i in range(32):
            if 1 << i > label:
                break
        result = []
        s = 1 << (i - 1)
        e = (1 << i) - 1
        if i % 2 == 0:
            label = (s + e - label)
        while label >= 1:
            s = 1 << (i - 1)
            e = (1 << i) - 1
            if i % 2 == 0:
                result.append(e + (s - label))
            else:
                result.append(label)
            label = label // 2
            i -= 1
        return reversed(result)
            