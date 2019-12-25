# title: contains-duplicate-iii
# detail: https://leetcode.com/submissions/detail/280595405/
# datetime: Thu Nov 21 19:08:18 2019
# runtime: 780 ms
# memory: 14.4 MB

import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0 or t < 0:
            return False
        N = len(nums)
        i = 0
        window = sorted(nums[i + 1: i + 1 + k])
        k = len(window)
        
        while i < N - 1:
            mi = (nums[i] - t)
            ma = (nums[i] + t)
            m = bisect.bisect_left(window, mi)
            n = bisect.bisect(window, ma)
            print(m, n)
            if n - m > 0:
                return True
            i += 1
            window.remove(nums[i])
            if i + k < N:
                bisect.insort(window, nums[i + k])
        return False
        
            
            
        