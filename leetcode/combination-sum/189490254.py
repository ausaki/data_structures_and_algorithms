# title: combination-sum
# detail: https://leetcode.com/submissions/detail/189490254/
# datetime: Wed Nov 14 15:02:43 2018
# runtime: 64 ms
# memory: N/A

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        return self._combinationSum(candidates, target)
    
    def _combinationSum(self, candidates, target, next_=0):
        result = []
        for i, c in enumerate(candidates[next_:]):
            if target < c:
                break
            if target == c:
                result.append([c])
                break
            else:
                parts = self._combinationSum(candidates, target - c, next_ + i)
                for p in parts:
                    p.insert(0, c)
                result.extend(parts)
        return result
        