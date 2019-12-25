# title: combination-sum-ii
# detail: https://leetcode.com/submissions/detail/189504588/
# datetime: Wed Nov 14 16:23:10 2018
# runtime: 32 ms
# memory: N/A

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        return self._combinationSum(candidates, target)
    
    def _combinationSum(self, candidates, target, next_=0):
        result = []
        prev_candidate = None
        for i, c in enumerate(candidates[next_:]):
            if target < c:
                break
            if c == prev_candidate:
                continue
            prev_candidate = c
            
            if target == c:
                result.append([c])
                break
            else:
                parts = self._combinationSum(candidates, target - c, next_ + i + 1)
                for p in parts:
                    p.insert(0, c)
                result.extend(parts)
        return result