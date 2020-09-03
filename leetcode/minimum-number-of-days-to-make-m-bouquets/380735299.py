# title: minimum-number-of-days-to-make-m-bouquets
# detail: https://leetcode.com/submissions/detail/380735299/
# datetime: Fri Aug 14 18:01:09 2020
# runtime: 1272 ms
# memory: 27.1 MB

from functools import lru_cache

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        days = bloomDay
        n = len(days)
        if n < m * k:
            return -1
        if n == m * k:
            return max(days)
        if k == 1:
            days.sort()
            return days[m - 1]
        min_day, max_day = min(days), max(days)
        while min_day < max_day:
            mid = (min_day + max_day) // 2
            flowers = 0
            adjs = 0
            for d in days:
                if d <= mid:
                    adjs += 1
                else:
                    flowers += adjs // k
                    adjs = 0
                    if flowers >= m:
                        break
            flowers += adjs // k
            if flowers >= m:
                max_day = mid
            else:
                min_day = mid + 1
        
        return min_day    
        
        
                        