# title: course-schedule-iv
# detail: https://leetcode.com/submissions/detail/381711377/
# datetime: Sun Aug 16 20:44:17 2020
# runtime: 1012 ms
# memory: 18.4 MB

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = collections.defaultdict(list)
        for c1, c2 in prerequisites:
            g[c2].append(c1)
        result = []
        # cache = {}
        @lru_cache(None)
        def query(c1, c2):
            if c1 == c2:
                return True
            if c2 not in g:
                return False
            for c in g[c2]:
                if query(c1, c):
                    return True
            return False
        
        for c1, c2 in queries:
            result.append(query(c1, c2))
        return result