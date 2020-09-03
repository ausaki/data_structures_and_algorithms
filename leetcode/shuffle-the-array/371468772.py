# title: shuffle-the-array
# detail: https://leetcode.com/submissions/detail/371468772/
# datetime: Sun Jul 26 00:45:10 2020
# runtime: 104 ms
# memory: 13.8 MB

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return itertools.chain.from_iterable((nums[i], nums[n + i]) for i in range(n))