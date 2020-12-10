# title: minimum-initial-energy-to-finish-tasks
# detail: https://leetcode.com/submissions/detail/422813726/
# datetime: Sun Nov 22 11:27:47 2020
# runtime: 2036 ms
# memory: 59.3 MB

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        def check(energy):
            for a, b in tasks:
                if energy < b:
                    return False
                energy -= a
            return True
        
        tasks.sort(key=lambda p: p[1] - p[0], reverse=True)
        l = sum(p[0] for p in tasks)
        r = sum(p[1] for p in tasks)
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l