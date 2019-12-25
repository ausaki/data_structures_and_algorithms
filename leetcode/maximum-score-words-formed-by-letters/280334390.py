# title: maximum-score-words-formed-by-letters
# detail: https://leetcode.com/submissions/detail/280334390/
# datetime: Wed Nov 20 19:56:25 2019
# runtime: 52 ms
# memory: 12.8 MB

from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters = Counter(letters)
        result = [0]
        
        def _dfs(i, n, letters):
            if i == len(words):
                if n > result[0]:
                    result[0] = n
                return
            
            counter = Counter(words[i])
            new_letters = letters.copy()
            m = n
            flag = True
            for char, cnt in counter.items():
                if cnt > letters.get(char, 0):
                    flag = False
                    break
                else:
                    new_letters[char] -= cnt
                    m += cnt * score[ord(char) - ord('a')]
            if flag:
                _dfs(i + 1, m, new_letters)
            _dfs(i + 1, n, letters)
        
        _dfs(0, 0, letters)
        return result[0]