# title: di-string-match
# detail: https://leetcode.com/submissions/detail/403462927/
# datetime: Fri Oct  2 17:02:12 2020
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
                a = x - k + 1
                for l in range(k):
                    result.append(a + l)
                x = a - 1
            if j == 'D':
                a = y + k - 1
                for l in range(k):
                    result.append(a - l)
                y = a + 1
        return result
                            
                