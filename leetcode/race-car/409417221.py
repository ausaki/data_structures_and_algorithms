# title: race-car
# detail: https://leetcode.com/submissions/detail/409417221/
# datetime: Fri Oct 16 18:25:11 2020
# runtime: 920 ms
# memory: 22.4 MB

class Solution:
    @lru_cache(None)
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        i = target.bit_length()
        if target == (1 << i) - 1:
            return i
        ins = i + 1 + self.racecar((1 << i) - 1 - target)
        for j in range(1, i):
            for k in range(j):
                ins = min(ins, j + k + 2 + self.racecar(target - (1 << j) + (1 << k)))
            # ins = min(ins, )
        return ins
                    
        
            
            