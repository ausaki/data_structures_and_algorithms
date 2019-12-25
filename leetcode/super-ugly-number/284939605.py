# title: super-ugly-number
# detail: https://leetcode.com/submissions/detail/284939605/
# datetime: Tue Dec 10 12:32:08 2019
# runtime: 288 ms
# memory: 16.6 MB

import heapq
    
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        def gen(prime):
            for num in nums:
                yield prime * num
        nums = [1]
        seq = heapq.merge(*map(gen, primes))
        while len(nums) < n:
            num = next(seq)
            if num != nums[-1]:
                nums.append(num)
        return nums[-1]
            