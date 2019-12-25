# title: letter-case-permutation
# detail: https://leetcode.com/submissions/detail/280118313/
# datetime: Tue Nov 19 23:01:18 2019
# runtime: 60 ms
# memory: 14 MB

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        def _dfs(i, s):
            if i == len(S):
                result.append(s)
                return
            if S[i].isdigit():
                _dfs(i + 1, s + S[i])
            else:
                _dfs(i + 1, s + S[i].lower())
                _dfs(i + 1, s + S[i].upper())
        _dfs(0, '')
        return result