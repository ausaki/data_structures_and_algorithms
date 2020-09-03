# title: number-of-sub-arrays-with-odd-sum
# detail: https://leetcode.com/submissions/detail/376881358/
# datetime: Thu Aug  6 16:00:58 2020
# runtime: 1232 ms
# memory: 17.5 MB

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        M = 10 ** 9 + 7
        odd = 0
        even = 0
        result = 0
        for i in arr:
            if i % 2:
                odd, even = even, odd
                odd += 1
            else:
                even += 1
            result = (result + odd) % M
        return result