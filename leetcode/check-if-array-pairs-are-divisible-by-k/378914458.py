# title: check-if-array-pairs-are-divisible-by-k
# detail: https://leetcode.com/submissions/detail/378914458/
# datetime: Mon Aug 10 23:46:23 2020
# runtime: 708 ms
# memory: 28.2 MB

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1: return True                                                                      
        counter = collections.Counter([((i % k) + k) % k for i in arr])
        while counter:
            num, cnt = counter.popitem()
            if (2 * num) % k == 0:
                if cnt % 2 != 0:
                    return False
                continue
            n = k - num
            if cnt == counter.get(n, 0):
                counter.pop(n)
                continue
            return False
        return True
        
                        
            
#         if k == 1: return True                                                                      
#         counter = collections.Counter([((i % k) + k) % k for i in arr])
#         def arrange():
#             if not counter:
#                 return True
#             num, cnt = counter.popitem()
#             if (2 * num) % k == 0:
#                 if cnt % 2 != 0:
#                     return False
#                 return arrange()
#             n = k - num  
#             if n in counter:
#                 if cnt == counter[n]:
#                     counter.pop(n)
#                     return arrange()
#                 return False
#             return False
        
#         return arrange()
                    
                