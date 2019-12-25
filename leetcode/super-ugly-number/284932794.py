# title: super-ugly-number
# detail: https://leetcode.com/submissions/detail/284932794/
# datetime: Tue Dec 10 12:00:01 2019
# runtime: 580 ms
# memory: 16.5 MB

import heapq
class Value:
    def __init__(self, prime, index, value):
        self.prime = prime
        self.index = index
        self.value = value
    
    def __lt__(self, right):
        return self.value < right.value
    def __eq__(self, right):
        return self.value == right.value
    def __gt(self, right):
        return self.value > right.value
    
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        index = dict.fromkeys(primes, 0)
        values = [Value(p, 0, p) for p in primes]
        heapq.heapify(values)
        nums = [1]
        while len(nums) < n:
            min_value = values[0].value
            nums.append(min_value)
            while values and values[0].value == min_value:
                val = heapq.heappop(values)
                val.index += 1
                val.value = val.prime * nums[val.index]
                heapq.heappush(values, val)
        return nums[-1]