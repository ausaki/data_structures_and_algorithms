# title: friends-of-appropriate-ages
# detail: https://leetcode.com/submissions/detail/409007348/
# datetime: Thu Oct 15 17:43:16 2020
# runtime: 392 ms
# memory: 14.9 MB

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        result = 0
        for i, age in enumerate(ages):
            j = bisect.bisect(ages, age // 2 + 7)
            k = bisect.bisect(ages, age, i)
            result += k - j - 1 if k - j - 1 > 0 else 0
        return result
        