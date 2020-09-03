# title: reducing-dishes
# detail: https://leetcode.com/submissions/detail/384256052/
# datetime: Sat Aug 22 00:27:22 2020
# runtime: 84 ms
# memory: 14 MB

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        if satisfaction[-1] <= 0:
            return 0
        i = bisect.bisect_left(satisfaction, 0)
        s0 = s = 0
        for j in range(i, n):
            s += (j - i + 1) * satisfaction[j]
            s0 += satisfaction[j]
        # print(s, s0, i)
        result = s
        s1 = 0
        for j in range(i - 1, -1, -1):
            s += s0 + satisfaction[j] + s1
            s1 += satisfaction[j]
            if s > result:
                result = s
            else:
                break
        return result