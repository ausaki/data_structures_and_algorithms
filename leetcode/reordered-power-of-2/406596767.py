# title: reordered-power-of-2
# detail: https://leetcode.com/submissions/detail/406596767/
# datetime: Fri Oct  9 23:47:39 2020
# runtime: 32 ms
# memory: 14 MB

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        pow2 = set()
        for i in range(30):
            pow2.add(''.join(sorted(str(1 << i))))
        return ''.join(sorted(str(N))) in pow2
