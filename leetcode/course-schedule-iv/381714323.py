# title: course-schedule-iv
# detail: https://leetcode.com/submissions/detail/381714323/
# datetime: Sun Aug 16 20:55:28 2020
# runtime: 820 ms
# memory: 17.1 MB

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = collections.defaultdict(list)
        for c1, c2 in prerequisites:
            g[c2].append(c1)
        result = []
        cache = {}
        def build_cache(c):
            if c not in g:
                return set()
            if c in cache:
                return cache[c]
            cache[c] = set()
            for c_ in g[c]:
                cache[c].update(build_cache(c_))
                cache[c].add(c_)
            return cache[c]
        
        for c in g:
            build_cache(c)
        
#         def query(c1, c2):
#             if c1 == c2:
#                 return True
#             if c2 not in g:
#                 return False
#             for c in g[c2]:
#                 if query(c1, c):
#                     return True
#             return False
        
        for c1, c2 in queries:
            result.append(c2 in cache and c1 in cache[c2])
        return result