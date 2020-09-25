# title: maximum-score-words-formed-by-letters
# detail: https://leetcode.com/submissions/detail/394514577/
# datetime: Sat Sep 12 15:24:21 2020
# runtime: 52 ms
# memory: 13.9 MB

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def dp(i):
            if i == len(words):
                return 0
            w = words[i]
            for k, v in w.items():
                if v > letters.get(k, 0):
                    break
            else:
                s1 = dp(i + 1)
                letters.subtract(w)
                s2 = sum(score[ord(k) - 97] * v for k, v in w.items())
                s2 += dp(i + 1)
                s = max(s1, s2)
                letters.update(w)
                return s
            return dp(i + 1)
            
        letters = collections.Counter(letters)
        for i, w in enumerate(words):
            words[i] = collections.Counter(w)
            
        return dp(0)