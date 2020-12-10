# title: defuse-the-bomb
# detail: https://leetcode.com/submissions/detail/420211084/
# datetime: Sun Nov 15 00:52:12 2020
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        ans = []
        s = sum(code[:k]) if k > 0 else sum(code[k - 1:-1])
        for i in range(n):
            if k > 0:
                s += code[(i + k) % n] - code[i]
            else:
                s += code[(i - 1) % n] - code[(i + k - 1) % n]
            ans.append(s)
        return ans