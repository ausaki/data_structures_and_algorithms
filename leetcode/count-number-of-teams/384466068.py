# title: count-number-of-teams
# detail: https://leetcode.com/submissions/detail/384466068/
# datetime: Sat Aug 22 11:19:54 2020
# runtime: 88 ms
# memory: 13.9 MB

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        result = 0
        for i in range(1, n - 1):
            lt = [0, 0]
            gt = [0, 0]
            for j in range(n):
                if rating[j] > rating[i]:
                    gt[0 if j < i else 1] += 1
                elif rating[j] < rating[i]:
                    lt[0 if j < i else 1] += 1
            result += lt[0] * gt[1] + gt[0] * lt[1]
        return result