# title: repeated-dna-sequences
# detail: https://leetcode.com/submissions/detail/278482423/
# datetime: Wed Nov 13 22:31:22 2019
# runtime: 76 ms
# memory: 24 MB

class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     seen = {}
    #     N = len(s)
    #     result = []
    #     for i in range(N - 9):
    #         k = s[i: i + 10]
    #         v = seen.get(k, 0)
    #         if v == 0:
    #             seen[k] = 1f
    #         elif v == 1:
    #             result.append(k)
    #             seen[k] += 1
    #         else:
    #             pass
    #     return result
    
     def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N = len(s)
        if N <= 10:
            return []
        seen = {}
        result = []
        encoding = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        mask = (1 << 20) - 1
        key = 0
        for i in range(10):
            key <<= 2
            key |= encoding[s[i]]
        seen[key] = 1
        for i in range(1, N - 9):
            key = (key << 2) & mask
            key |= encoding[s[i + 9]]
            v = seen.get(key, 0)
            if v == 0:
                seen[key] = 1
            elif v == 1:
                result.append(s[i: i + 10])
                seen[key] += 1
            else:
                pass
        return result
        