# title: path-in-zigzag-labelled-binary-tree
# detail: https://leetcode.com/submissions/detail/397397500/
# datetime: Fri Sep 18 16:21:59 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        i = 1
        for i in range(32):
            if 1 << i > label:
                break
        j = i
        result = []
        while label >= 1:
            s = 1 << (i - 1)
            e = (1 << i) - 1
            if i < j and i % 2 == 0:
                label = (e + (s - label))
            result.append(label)
            if i % 2:
                label = label // 2
            else:
                label = (s + (e - label)) // 2
            i -= 1
        return reversed(result)
            