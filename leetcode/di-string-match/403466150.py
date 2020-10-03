# title: di-string-match
# detail: https://leetcode.com/submissions/detail/403466150/
# datetime: Fri Oct  2 17:16:25 2020
# runtime: 64 ms
# memory: 15.1 MB

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        x = len(S)
        y = 0
        result = []
        for i in S:
            if i == 'I':
                result.append(y)
                y += 1
            else:
                result.append(x)
                x -= 1
        result.append(y)
        return result
                            
                