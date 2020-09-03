# title: count-number-of-teams
# detail: https://leetcode.com/submissions/detail/384462157/
# datetime: Sat Aug 22 11:05:52 2020
# runtime: 1236 ms
# memory: 13.9 MB

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        result = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        result += 1
        return result