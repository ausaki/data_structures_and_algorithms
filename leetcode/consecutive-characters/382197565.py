# title: consecutive-characters
# detail: https://leetcode.com/submissions/detail/382197565/
# datetime: Mon Aug 17 20:42:09 2020
# runtime: 40 ms
# memory: 13.9 MB

class Solution:
    def maxPower(self, s: str) -> int:
        cnt = 0
        power = 0
        prev = ''
        for ch in s:
            if ch == prev:
                cnt += 1
            else:
                cnt = 1
            power = max(power, cnt)
            prev = ch
        return power