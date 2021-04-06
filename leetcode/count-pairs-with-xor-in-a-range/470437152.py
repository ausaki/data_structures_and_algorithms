# title: count-pairs-with-xor-in-a-range
# detail: https://leetcode.com/submissions/detail/470437152/
# datetime: Sun Mar 21 12:25:00 2021
# runtime: 6492 ms
# memory: 20.4 MB

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        n = len(nums)
        root = [None, None, 0]
        
        def count_bigger(x, low):
            curr = root
            cnt = 0
            for i in reversed(range(31)):
                b1 = (low >> i) & 1
                b2 = (x >> i) & 1
                if b1 == 0:
                    if curr[1 - b2]:
                        cnt += curr[1 - b2][2]
                    curr = curr[b2]
                else:
                    curr = curr[1 - b2]
                if curr is None:
                    break
            return cnt
        
        def insert(x):
            curr = root
            for i in reversed(range(31)):
                b = (x >> i) & 1
                if curr[b] is None:
                    curr[b] = [None, None, 0]
                curr = curr[b]
                curr[2] += 1
                
        a, b = 0, 0
        for i in nums:
            a += count_bigger(i, low - 1)
            b += count_bigger(i, high)
            insert(i)    
        return a - b