# title: pyramid-transition-matrix
# detail: https://leetcode.com/submissions/detail/280112877/
# datetime: Tue Nov 19 22:23:35 2019
# runtime: 36 ms
# memory: 12.7 MB

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def _dfs(bottom, top, i):
            if len(bottom) == 1:
                return True
            if i == len(bottom) - 1:
                return _dfs(top, '', 0)
            candidates = allowed.get(bottom[i: i + 2])
            if candidates is None:
                return False
            for c in candidates:
                if _dfs(bottom, top + c, i + 1):
                    return True
            return False
    
        new_allowed = {}
        for s in allowed:
            new_allowed.setdefault(s[:2], []).append(s[2])
        allowed = new_allowed
        
        return _dfs(bottom, '', 0)
    
