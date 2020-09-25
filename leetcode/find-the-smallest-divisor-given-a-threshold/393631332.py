# title: find-the-smallest-divisor-given-a-threshold
# detail: https://leetcode.com/submissions/detail/393631332/
# datetime: Thu Sep 10 14:38:53 2020
# runtime: 380 ms
# memory: 19.6 MB

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n == 1:
            return (nums[0] + threshold - 1) // threshold
        nums.sort()
        print(nums)
        maxsum = sum(nums)
        minsum = n
        if threshold >= maxsum:
            return 1
        if threshold <= minsum:
            return nums[-1]
        i, j = 0, n - 1
        while i <= j:
            m = (i + j) // 2
            s0 = m + 1
            div = nums[m]
            for k in range(m + 1, n):
                s0 += (nums[k] + div - 1) // div
            if s0 <= threshold:
                j = m - 1            
            else:
                i = m + 1
        # print(i, j)
        l = (nums[i - 1] + 1) if i else 2
        r = nums[i]
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m)
            s0 = i
            for k in range(i, n):
                s0 += (nums[k] + m - 1) // m
            # print(s0)
            if s0 <= threshold:
                r = m - 1
            else:
                l = m + 1
        return l
            
        
        