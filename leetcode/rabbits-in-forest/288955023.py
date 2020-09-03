# title: rabbits-in-forest
# detail: https://leetcode.com/submissions/detail/288955023/
# datetime: Fri Dec 27 21:00:59 2019
# runtime: 36 ms
# memory: 13 MB

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = collections.Counter(answers)
        res = 0
        for k, c in cnt.items():
            if k == 0:
                res += c
            else:
                while k + 1 < c:
                    res += k + 1
                    c -= k + 1
                res += k + 1
        return res
                    
        