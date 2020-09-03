# title: check-if-array-pairs-are-divisible-by-k
# detail: https://leetcode.com/submissions/detail/378907740/
# datetime: Mon Aug 10 23:28:40 2020
# runtime: 696 ms
# memory: 64.6 MB

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1: return True                                                                      
        counter = collections.Counter([((i % k) + k) % k for i in arr])
        MAX = max(counter)
        def arrange():
            if not counter:
                return True
            num, cnt = counter.popitem()
            if (2 * num) % k == 0:
                return cnt % 2 == 0
            if not counter:
                return cnt == 0
            n = k - num  
            if n in counter:
                if cnt == counter[n]:
                    counter.pop(n)
                    return arrange()
                return False
            return False
        
        return arrange()
                        
                    
                