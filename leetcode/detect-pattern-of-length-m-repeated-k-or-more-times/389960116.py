# title: detect-pattern-of-length-m-repeated-k-or-more-times
# detail: https://leetcode.com/submissions/detail/389960116/
# datetime: Wed Sep  2 21:55:13 2020
# runtime: 24 ms
# memory: 14 MB

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        cnt = 0 
        for i in range(n - m):
            if arr[i] == arr[i + m]:
                cnt += 1
            else:
                cnt = 0
            if cnt == (k - 1) * m:
                return True
        return False
            
                
            
                
            