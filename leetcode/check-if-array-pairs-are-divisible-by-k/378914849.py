# title: check-if-array-pairs-are-divisible-by-k
# detail: https://leetcode.com/submissions/detail/378914849/
# datetime: Mon Aug 10 23:47:24 2020
# runtime: 724 ms
# memory: 27.9 MB

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1: return True                                                                      
        counter = collections.Counter(((i % k) + k) % k for i in arr)
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
                