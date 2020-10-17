# title: fair-candy-swap
# detail: https://leetcode.com/submissions/detail/405967935/
# datetime: Thu Oct  8 11:26:50 2020
# runtime: 336 ms
# memory: 16.3 MB

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A)) // 2
        B = set(B)
        for a in A:
            if a + diff in B:
                return [a, a + diff]
        
                