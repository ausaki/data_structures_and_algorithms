# title: friends-of-appropriate-ages
# detail: https://leetcode.com/submissions/detail/409015151/
# datetime: Thu Oct 15 18:23:18 2020
# runtime: 240 ms
# memory: 14.8 MB

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        buckets = [0] * 121
        for age in ages:
            buckets[age] += 1
        low = 15
        s = 0
        result = 0
        for age in range(15, 121):
            cnt = buckets[age]
            low1 = age // 2 + 7
            s += cnt
            while low <= low1:
                s -= buckets[low]
                low += 1
            result +=  cnt * (s - 1)
        return result
        