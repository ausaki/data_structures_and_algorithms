# title: divide-array-in-sets-of-k-consecutive-numbers
# detail: https://leetcode.com/submissions/detail/392855162/
# datetime: Tue Sep  8 23:47:27 2020
# runtime: 460 ms
# memory: 29.3 MB

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter(nums)
        keys = sorted(counter)
        for i in keys:
            if counter[i] <= 0:
                continue
            for j in reversed(range(k)):
                counter[i + j] -= counter[i]
                if counter[i + j] < 0:
                    return False
        return True 
            