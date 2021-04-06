# title: evaluate-the-bracket-pairs-of-a-string
# detail: https://leetcode.com/submissions/detail/473267088/
# datetime: Sun Mar 28 11:01:32 2021
# runtime: 984 ms
# memory: 54.8 MB

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        vals = dict(knowledge)
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = s.find('(', i)
            if j == -1:
                res.append(s[i:])
                break
            k = s.find(')', j)
            res.append(s[i: j])
            res.append(vals.get(s[j + 1: k], '?'))
            i = k + 1
        return ''.join(res)
            