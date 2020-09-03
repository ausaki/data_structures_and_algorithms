# title: maximum-points-you-can-obtain-from-cards
# detail: https://leetcode.com/submissions/detail/383166100/
# datetime: Wed Aug 19 18:44:13 2020
# runtime: 460 ms
# memory: 27.1 MB

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        k = n - k
        s = sum(cardPoints[k:])
        result = s
        for i in range(k, n):
            s += cardPoints[i - k] - cardPoints[i]
            result = max(result, s)
        return result
        