# title: number-of-sub-arrays-with-odd-sum
# detail: https://leetcode.com/submissions/detail/376880706/
# datetime: Thu Aug  6 15:59:11 2020
# runtime: 2444 ms
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
            # print(odd, even)
            result += odd
        return result % M