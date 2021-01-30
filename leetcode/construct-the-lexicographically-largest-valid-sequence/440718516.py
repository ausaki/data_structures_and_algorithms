# title: construct-the-lexicographically-largest-valid-sequence
# detail: https://leetcode.com/submissions/detail/440718516/
# datetime: Sat Jan  9 23:37:06 2021
# runtime: 68 ms
# memory: 14.4 MB

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = (2 * (n - 1) + 1)
        res = [0] * m
        nums = list(range(n + 1))
        
        def dfs(i):
            if i == m:
                return res
            if res[i] != 0:
                return dfs(i + 1)
            for j in reversed(range(1, n + 1)):
                if not nums[j]:
                    continue
                if j == 1:
                    nums[j] = False
                    res[i] = j
                    r = dfs(i + 1)
                    if r:
                        return r
                    nums[j] = True
                    res[i] = 0
                elif i + j < m and res[i + j] == 0:
                    nums[j] = False
                    res[i] = res[i + j] = j
                    r = dfs(i + 1)
                    if r:
                        return r
                    nums[j] = True
                    res[i] = res[i + j] = 0
            return []
        
        return dfs(0)