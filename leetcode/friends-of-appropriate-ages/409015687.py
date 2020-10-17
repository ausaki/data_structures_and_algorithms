# title: friends-of-appropriate-ages
# detail: https://leetcode.com/submissions/detail/409015687/
# datetime: Thu Oct 15 18:26:24 2020
# runtime: 268 ms
# memory: 14.7 MB

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        buckets = [0] * 121
        max_age = 0
        for age in ages:
            buckets[age] += 1
            max_age = max(max_age, age)
        low = 15
        s = 0
        result = 0
        for age in range(15, max_age + 1):
            cnt = buckets[age]
            low1 = age // 2 + 7
            s += cnt
            while low <= low1:
                s -= buckets[low]
                low += 1
            result +=  cnt * (s - 1)
        return result
        