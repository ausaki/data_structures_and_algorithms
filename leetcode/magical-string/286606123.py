# title: magical-string
# detail: https://leetcode.com/submissions/detail/286606123/
# datetime: Tue Dec 17 17:46:05 2019
# runtime: 180 ms
# memory: 13.2 MB

class Solution:
    def magicalString(self, n: int) -> int:
        if n < 1: return 0
        if n <= 3: return 1
        i = 3
        res = 1
        queue = collections.deque([2])
        while i <= n:
            j = queue[0]
            k = 2 if queue[-1] == 1 else 1
            queue.append(k)
            if j == 2: queue.append(k)
            j = queue.popleft()                    
            if j == 1: res += 1
            i += 1
        return res