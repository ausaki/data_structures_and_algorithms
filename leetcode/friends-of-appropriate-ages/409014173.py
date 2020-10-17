# title: friends-of-appropriate-ages
# detail: https://leetcode.com/submissions/detail/409014173/
# datetime: Thu Oct 15 18:17:47 2020
# runtime: 240 ms
# memory: 14.7 MB

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        buckets = [0] * 121
        for age in ages:
            buckets[age] += 1
        s = 0
        low = 0
        result = 0
        for age, cnt in enumerate(buckets):
            # if cnt == 0:
            #     continue
            low1 = age // 2 + 7
            s += cnt
            if low1 >= age:
                continue
            while low <= low1:
                s -= buckets[low]
                low += 1
            result +=  cnt * (s - 1)
        return result
        