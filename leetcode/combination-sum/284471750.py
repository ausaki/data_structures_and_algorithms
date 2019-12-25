# title: combination-sum
# detail: https://leetcode.com/submissions/detail/284471750/
# datetime: Sun Dec  8 12:18:14 2019
# runtime: 48 ms
# memory: 12.8 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        def _find(target, i):
            result = []
            for j in range(i, N):
                if target < candidates[j]:
                    break
                if target == candidates[j]:
                    result.append([candidates[j]])
                    break
                else:
                    parts = _find(target - candidates[j], j)
                    for p in parts:
                        p.insert(0, candidates[j])
                    result.extend(parts)
            return result
        
        return _find(target, 0)