# title: k-concatenation-maximum-sum
# detail: https://leetcode.com/submissions/detail/281062606/
# datetime: Sat Nov 23 23:03:10 2019
# runtime: 340 ms
# memory: 26 MB

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        result = 0
        N = len(arr)
        lo = -1
        hi = -1
        prev = -1
        prev_lo = -1
        prev_hi = -1
        for i in range(min(2, k)):
            for j in range(N):
                if prev > 0:
                    prev_hi = (i * N) + j
                    s = arr[j] + prev
                else:
                    s = arr[j]
                    prev_lo = prev_hi = (i * N) + j
                prev = s
                if s > result:
                    lo = prev_lo
                    hi = prev_hi
                    result = s
        if result == 0 or hi < N:
            return result % (10 ** 9 + 7)
        hi = hi % N
        # if lo == 0 and hi == N - 1:
        #     result = result // 2 * k
        if lo <= hi + 1:
            result = result + (result - sum(arr[lo:hi + 1])) * (k - 2)
        return result % (10 ** 9 + 7)