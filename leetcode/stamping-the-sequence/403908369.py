# title: stamping-the-sequence
# detail: https://leetcode.com/submissions/detail/403908369/
# datetime: Sat Oct  3 21:27:41 2020
# runtime: 144 ms
# memory: 14.3 MB

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        stamp = list(stamp)
        target = list(target)
        result = []
        
        def change(i):
            if target[i:i + m].count('?') == m:
                return False
            ch = False
            for j in range(m):
                if target[i + j] == '?':
                    continue
                if target[i + j] != stamp[j]:
                    ch = False
                    break
                ch = True
            if ch:
                target[i:i + m] = ['?'] * m
                result.append(i)
            return ch
        ch = True
        while ch:
            ch = False
            for i in range(n - m + 1):
                ch |= change(i)
            
        return reversed(result) if target.count('?') == n else []