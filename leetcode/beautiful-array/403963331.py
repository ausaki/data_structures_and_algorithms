# title: beautiful-array
# detail: https://leetcode.com/submissions/detail/403963331/
# datetime: Sat Oct  3 23:48:34 2020
# runtime: 60 ms
# memory: 14.5 MB

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        result = list(range(1, N + 1))
        def partition(i, j):
            if j - i <= 2: return
            result[i:j] = result[i:j:2] + result[i + 1:j:2]
            m = i + (j - i + 1) // 2
            partition(i, m)
            partition(m, j)
        
        partition(0, N)
        return result