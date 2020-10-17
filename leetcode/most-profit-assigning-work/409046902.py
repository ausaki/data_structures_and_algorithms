# title: most-profit-assigning-work
# detail: https://leetcode.com/submissions/detail/409046902/
# datetime: Thu Oct 15 21:04:53 2020
# runtime: 400 ms
# memory: 16.2 MB

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs = sorted(([d, p] for d, p in zip(difficulty, profit)), key=lambda item: item[0])
        for i in range(1, len(pairs)):
            pairs[i][1] = max(pairs[i][1], pairs[i - 1][1])
        result = 0
        for w in worker:
            i = bisect.bisect(pairs, [w, 10 ** 5])
            result += pairs[i - 1][1] if i else 0
        return result
            