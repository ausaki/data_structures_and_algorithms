# title: minimum-number-of-days-to-make-m-bouquets
# detail: https://leetcode.com/submissions/detail/380726940/
# datetime: Fri Aug 14 17:27:44 2020
# runtime: 2348 ms
# memory: 31.9 MB

from functools import lru_cache

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        days = sorted(zip(bloomDay, range(n)))
        max_day = days[-1][0]
        adjs = [[-1, -1], [n, n]]
        flowers = 0
        for day, idx in days:
            i = bisect.bisect(adjs, [idx])
            # print(day, idx, adjs, i)
            if idx == adjs[i - 1][1] + 1:
                if idx + 1 == adjs[i][0]:
                    a = adjs[i - 1][1] - adjs[i - 1][0] + 1
                    if i - 1 == 0:
                        a -= 1
                    b = adjs[i][1] - adjs[i][0] + 1
                    if i == len(adjs) - 1:
                        b -= 1
                    f1 = a // k
                    f2 = b // k
                    f = (a + b + 1) // k
                    flowers += f - f1 - f2
                    adjs[i - 1][1] = adjs[i][1]
                    adjs.pop(i)
                else:
                    a = adjs[i - 1][1] - adjs[i - 1][0] + 1
                    if i - 1 == 0:
                        a -= 1
                    f1 = a // k
                    f = (a + 1) // k
                    flowers += f - f1
                    adjs[i - 1][1] += 1
            else:
                if idx + 1 == adjs[i][0]:
                    b = adjs[i][1] - adjs[i][0] + 1
                    if i == len(adjs) - 1:
                        b -= 1
                    f2 = b // k
                    f = (b + 1) // k
                    flowers += f - f2
                    adjs[i][0] -= 1
                else:
                    adjs.insert(i, [idx, idx])
                    flowers += 1 // k
            # print(flowers)
            if flowers == m:
                return day
        return -1
                        