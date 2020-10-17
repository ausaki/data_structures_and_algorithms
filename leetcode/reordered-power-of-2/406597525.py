# title: reordered-power-of-2
# detail: https://leetcode.com/submissions/detail/406597525/
# datetime: Fri Oct  9 23:50:10 2020
# runtime: 32 ms
# memory: 14.2 MB

class Solution:
    pow2 = set()
    for i in range(30):
        pow2.add(''.join(sorted(str(1 << i))))
    def reorderedPowerOf2(self, N: int) -> bool:
        return ''.join(sorted(str(N))) in self.pow2
