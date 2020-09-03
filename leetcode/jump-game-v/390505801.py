# title: jump-game-v
# detail: https://leetcode.com/submissions/detail/390505801/
# datetime: Thu Sep  3 23:25:40 2020
# runtime: 580 ms
# memory: 16.8 MB

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        @lru_cache(None)
        def jump(i):
            result = 0
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                result = max(result, jump(j))
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                result = max(result, jump(j))
            return result + 1
        
        return max(jump(i) for i in range(n))