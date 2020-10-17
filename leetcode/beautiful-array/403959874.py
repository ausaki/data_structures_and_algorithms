# title: beautiful-array
# detail: https://leetcode.com/submissions/detail/403959874/
# datetime: Sat Oct  3 23:40:27 2020
# runtime: 44 ms
# memory: 14.4 MB

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        result = list(range(1, N + 1))
        def partition(i, j):
            if j - i <= 2: return
            odd = result[i:j:2]
            even = result[i + 1:j:2]
            result[i:j] = odd + even
            partition(i, i + len(odd))
            partition(i + len(odd), j)
        
        partition(0, N)
        return result