# title: poor-pigs
# detail: https://leetcode.com/submissions/detail/429572610/
# datetime: Fri Dec 11 22:50:15 2020
# runtime: 32 ms
# memory: 14.3 MB

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest / minutesToDie + 1))