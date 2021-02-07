# title: largest-merge-of-two-strings
# detail: https://leetcode.com/submissions/detail/453067453/
# datetime: Sun Feb  7 13:11:23 2021
# runtime: 1872 ms
# memory: 14.5 MB

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        i, j = 0, 0
        
        while i < n and j < m:
            if word1[i] > word2[j]:
                res.append(word1[i])
                i += 1
                continue
            elif word1[i] < word2[j]:
                res.append(word2[j])
                j += 1
                continue
            ii, jj = i, j
            while ii < n and jj < m and word1[ii] == word2[jj]:
                ii += 1
                jj += 1
            if ii >= n or (jj < m and word1[ii] < word2[jj]):
                res.append(word2[j])
                j += 1
            else:
                res.append(word1[i])
                i += 1
        if i < n:
            res.extend(word1[i:])
        if j < m:
            res.extend(word2[j:])
        return ''.join(res)