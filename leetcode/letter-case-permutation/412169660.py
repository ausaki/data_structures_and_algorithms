# title: letter-case-permutation
# detail: https://leetcode.com/submissions/detail/412169660/
# datetime: Fri Oct 23 14:36:57 2020
# runtime: 60 ms
# memory: 15.3 MB

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = list(S)
        n = len(s)
        result = []
        def permutation(i):
            if i == n:
                result.append(''.join(s))
                return
            permutation(i + 1)
            if s[i].isalpha():
                s[i] = s[i].swapcase()
                permutation(i + 1)
                s[i] = s[i].swapcase()
        permutation(0)
        return result