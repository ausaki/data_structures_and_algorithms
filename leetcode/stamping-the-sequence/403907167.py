# title: stamping-the-sequence
# detail: https://leetcode.com/submissions/detail/403907167/
# datetime: Sat Oct  3 21:23:01 2020
# runtime: 1168 ms
# memory: 14.2 MB

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        stamp = list(stamp)
        target = list(target)
        result = []
        
        def change(i):
            if target[i:i + m].count('?') == m:
                return False
            if all(target[i + j] == '?' or target[i + j] == stamp[j] for j in range(m)):
                target[i:i + m] = ['?'] * m
                result.append(i)
                return True
            return False
        while True:
            if not any(change(i) for i in range(n - m + 1)):
                break
        return reversed(result) if target.count('?') == n else []