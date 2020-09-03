# title: range-sum-of-sorted-subarray-sums
# detail: https://leetcode.com/submissions/detail/377926941/
# datetime: Sat Aug  8 23:37:04 2020
# runtime: 76 ms
# memory: 14 MB

from collections import deque


class Solution:
    def rangeSum(self, nums: List[int], _: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        
        def subarray_with_sum_at_most(max_sum):
            window = deque()  # window
            cnt, s = 0, 0
            sw, tri_sw = 0, 0
            # sum of window, sum(i * x for i, x in enum(window))
            for x in nums:
                window.append(x)
                sw, tri_sw = sw + x, tri_sw + len(window) * x
                while sw > max_sum:
                    sw, tri_sw = sw - window.popleft(), tri_sw - sw

                cnt += len(window)
                s += tri_sw

            return cnt, s
        
        def find_k_smallest_subarray_sum(k):
            if k == 0:
                return 0
            elif k == 1:
                return min(nums)
            lo, hi = min(nums), sum(nums)
            while lo < hi:
                mid = (lo + hi) >> 1
                n_sub, sum_sub = subarray_with_sum_at_most(mid)
                if n_sub > k:
                    hi = mid - 1
                elif n_sub < k:
                    lo = mid + 1
                else:
                    return sum_sub

            n_sub, sum_sub = subarray_with_sum_at_most(lo)
            if n_sub < k:
                return sum_sub + (k - n_sub) * (lo + 1)
            else:
                return sum_sub - (n_sub - k) * lo

        return (
            find_k_smallest_subarray_sum(right)
            - find_k_smallest_subarray_sum(left - 1)
        ) % MOD
