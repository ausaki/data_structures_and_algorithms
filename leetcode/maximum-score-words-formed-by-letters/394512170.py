# title: maximum-score-words-formed-by-letters
# detail: https://leetcode.com/submissions/detail/394512170/
# datetime: Sat Sep 12 15:15:59 2020
# runtime: 40 ms
# memory: 14 MB

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
                s2 = 0
                for k, v in w.items():
                    letters[k] -= v
                    s2 += score[ord(k) - 97] * v
                s2 += dp(i + 1)
                s = max(s1, s2)
                for k, v in w.items():
                    letters[k] += v
                return s
            return dp(i + 1)
            
        letters = collections.Counter(letters)
        for i, w in enumerate(words):
            words[i] = collections.Counter(w)
            
        return dp(0)