# title: shuffle-the-array
# detail: https://leetcode.com/submissions/detail/371469971/
# datetime: Sun Jul 26 00:48:23 2020
# runtime: 64 ms
# memory: 14 MB

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # return itertools.chain.from_iterable((nums[i], nums[n + i]) for i in range(n))
        a = [0] * (2 * n)
        for i in range(n):
            a[2 * i] = nums[i]
            a[2 * i + 1] = nums[n + i]
        return a