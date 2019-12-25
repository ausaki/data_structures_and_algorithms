# title: repeated-dna-sequences
# detail: https://leetcode.com/submissions/detail/278479065/
# datetime: Wed Nov 13 22:06:03 2019
# runtime: 68 ms
# memory: 26.4 MB

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        N = len(s)
        result = []
        for i in range(N - 9):
            k = s[i: i + 10]
            v = seen.get(k, 0)
            if v == 0:
                seen[k] = 1
            elif v == 1:
                result.append(k)
                seen[k] += 1
            else:
                pass
        return result
        