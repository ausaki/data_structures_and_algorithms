# title: di-string-match
# detail: https://leetcode.com/submissions/detail/403464969/
# datetime: Fri Oct  2 17:11:21 2020
# runtime: 80 ms
# memory: 15.4 MB

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        ID = [[S[0], 1]]
        for i in range(1, n):
            if S[i] == ID[-1][0]:
                ID[-1][1] += 1
            else:
                ID.append([S[i], 1])
        x = n
        y = 0
        result = []
        for j, k in ID:
            if not result:
                k += 1
            if j == 'I':
                for l in reversed(range(k)):
                    result.append(x - l)
                x -= k
            if j == 'D':
                for l in reversed(range(k)):
                    result.append(y + l)
                y += k
        return result
                            
                