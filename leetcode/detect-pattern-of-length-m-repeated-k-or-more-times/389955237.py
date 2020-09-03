# title: detect-pattern-of-length-m-repeated-k-or-more-times
# detail: https://leetcode.com/submissions/detail/389955237/
# datetime: Wed Sep  2 21:40:32 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        i = 0
        for i in range(n - m * k + 1):
            for j in range(i + m, i + (k - 1) * m + 1, m):
                for l in range(m):
                    if arr[i + l] != arr[j + l]:
                        break
                else:
                    continue
                break
            else:
                return True
        return False
            
                
            
                
            