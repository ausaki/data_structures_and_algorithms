# title: race-car
# detail: https://leetcode.com/submissions/detail/409417594/
# datetime: Fri Oct 16 18:27:23 2020
# runtime: 36 ms
# memory: 14.6 MB

class Solution:
    @lru_cache(None)
    def racecar(self, target: int) -> int:
        i = target.bit_length()
        if target == (1 << i) - 1:
            return i
        ins = i + 1 + self.racecar((1 << i) - 1 - target)
        for j in range(i - 1):
            ins = min(ins, i + j + 1 + self.racecar(target - (1 << (i - 1)) + (1 << j)))
        return ins
                    
        
            
            