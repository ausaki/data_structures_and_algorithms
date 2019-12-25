# title: super-ugly-number
# detail: https://leetcode.com/submissions/detail/284944393/
# datetime: Tue Dec 10 12:53:44 2019
# runtime: 308 ms
# memory: 16.6 MB

import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        def gen(prime):
            for num in nums:
                yield prime * num
        nums = [1]
        seqs = [gen(p) for p in primes]
        values = []
        for i, seq in enumerate(seqs):
            try:
                values.append((next(seq), i))
            except StopIteration:
                continue
        heapq.heapify(values)
        while len(nums) < n:
            num, i = heapq.heappop(values)
            if num != nums[-1]:
                nums.append(num)
            try:
                heapq.heappush(values, (next(seqs[i]), i))
            except StopIteration:
                pass
        return nums[-1]
            