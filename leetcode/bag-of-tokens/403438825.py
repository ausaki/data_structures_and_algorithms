# title: bag-of-tokens
# detail: https://leetcode.com/submissions/detail/403438825/
# datetime: Fri Oct  2 15:30:58 2020
# runtime: 60 ms
# memory: 14.3 MB

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        max_points, points = 0, 0
        tokens.sort()
        i, j = 0, len(tokens) - 1
        while i <= j:
            if P < tokens[i]:
                if i == j or points == 0: break
                P += tokens[j]
                points -= 1
                j -= 1
            points += 1
            P -= tokens[i]
            i += 1
            max_points = max(max_points, points)
        return max_points