# title: find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
# detail: https://leetcode.com/submissions/detail/383626126/
# datetime: Thu Aug 20 16:03:57 2020
# runtime: 28 ms
# memory: 13.7 MB

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-2] + fibs[-1])
        cnt = 0
        for i in reversed(fibs):
            if k == 0:
                break
            if k >= i:
                k -= i
                cnt += 1
        return cnt        
        
        