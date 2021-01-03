# title: ways-to-split-array-into-three-subarrays
# detail: https://leetcode.com/submissions/detail/437815658/
# datetime: Sun Jan  3 11:34:34 2021
# runtime: 3948 ms
# memory: 27.3 MB

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        def find(l, r, i):
            while l <= r:
                m = (l + r) // 2
                s2 = prefix[m + 1] - prefix[i + 1]
                s3 = prefix[-1] - prefix[m + 1]
                if s3 >= s2:
                    l = m + 1
                else:
                    r = m - 1
            return r
            
        n = len(nums)
        if n == 3:
            return 1 if nums[0] <=  nums[1] <= nums[2] else 0
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        res = 0
        for i in range(n - 2):
            s1 = prefix[i + 1]
            j = bisect.bisect_left(prefix, s1 + s1, i + 2)
            if j >= n + 1:
                continue
            k = find(j - 1, n - 2, i)
            res = (res + k - (j - 1) + 1) % MOD
        return res
            
                