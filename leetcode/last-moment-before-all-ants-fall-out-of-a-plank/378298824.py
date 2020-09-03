# title: last-moment-before-all-ants-fall-out-of-a-plank
# detail: https://leetcode.com/submissions/detail/378298824/
# datetime: Sun Aug  9 15:38:04 2020
# runtime: 176 ms
# memory: 14.6 MB

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))