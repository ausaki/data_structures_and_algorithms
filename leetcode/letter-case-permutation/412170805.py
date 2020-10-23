# title: letter-case-permutation
# detail: https://leetcode.com/submissions/detail/412170805/
# datetime: Fri Oct 23 14:41:02 2020
# runtime: 52 ms
# memory: 15.1 MB

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = list(S)
        idx = [i for i, c in enumerate(s) if c.isalpha()]
        n = len(idx)
        result = []
        def permutation(i):
            if i == n:
                result.append(''.join(s))
                return
            permutation(i + 1)
            j = idx[i]
            s[j] = s[j].swapcase()
            permutation(i + 1)
            s[j] = s[j].swapcase()
        permutation(0)
        return result