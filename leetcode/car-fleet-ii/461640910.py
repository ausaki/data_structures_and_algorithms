# title: car-fleet-ii
# detail: https://leetcode.com/submissions/detail/461640910/
# datetime: Sun Feb 28 16:43:07 2021
# runtime: 1760 ms
# memory: 59.8 MB

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1] * n
        prev = [n - 1]
        for i in range(n - 2, -1, -1):
            p, s = cars[i]
            while prev and s <= cars[prev[-1]][1]:
                prev.pop()
            while prev:
                j = prev[-1]
                pp, ss = cars[j]
                sec = (pp - p) / (s - ss)
                if ans[j] == -1 or sec <= ans[j]:
                    ans[i] = sec
                    break
                else:
                    prev.pop()
            prev.append(i)
        return ans
        