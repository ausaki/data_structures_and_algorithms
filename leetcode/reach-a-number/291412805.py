# title: reach-a-number
# detail: https://leetcode.com/submissions/detail/291412805/
# datetime: Sun Jan  5 20:58:22 2020
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(math.sqrt(target * 2))
        s = n * (n + 1) // 2
        while s > target:
            s -= n
            n -= 1
        if s == target:
            return n
        n += 1
        s += n
        while (s - target) % 2:
            n += 1
            s += n
        return n