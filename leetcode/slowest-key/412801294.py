# title: slowest-key
# detail: https://leetcode.com/submissions/detail/412801294/
# datetime: Sun Oct 25 10:38:49 2020
# runtime: 80 ms
# memory: 14.4 MB

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ma = (-1, '')
        for i, (r, k) in enumerate(zip(releaseTimes, keysPressed)):
            t = r - (releaseTimes[i - 1] if i else 0)
            ma = max(ma, (t, k))
        return ma[1]