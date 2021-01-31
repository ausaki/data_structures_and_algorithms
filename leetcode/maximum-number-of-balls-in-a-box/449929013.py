# title: maximum-number-of-balls-in-a-box
# detail: https://leetcode.com/submissions/detail/449929013/
# datetime: Sun Jan 31 10:38:36 2021
# runtime: 656 ms
# memory: 14.4 MB

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        return collections.Counter(sum(map(int, str(i))) for i in range(lowLimit, highLimit + 1)).most_common(1)[0][1]