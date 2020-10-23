# title: rabbits-in-forest
# detail: https://leetcode.com/submissions/detail/412255059/
# datetime: Fri Oct 23 21:32:01 2020
# runtime: 44 ms
# memory: 14.3 MB

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum((v + k - 1) // k * k for k, v in collections.Counter(a + 1 for a in answers).items())