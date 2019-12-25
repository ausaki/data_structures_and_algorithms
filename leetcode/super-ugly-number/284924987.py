# title: super-ugly-number
# detail: https://leetcode.com/submissions/detail/284924987/
# datetime: Tue Dec 10 11:24:03 2019
# runtime: 1064 ms
# memory: 16.5 MB

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        index = dict.fromkeys(primes, 0)
        nums = [1]
        while len(nums) < n:
            values = [(k, k * nums[i]) for k, i in index.items()]
            _, min_value = min(values, key=lambda item: item[1])
            for k, v in values:
                if v == min_value:
                    index[k] += 1
            nums.append(min_value)
        return nums[-1]