# title: check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
# detail: https://leetcode.com/submissions/detail/381727943/
# datetime: Sun Aug 16 21:44:23 2020
# runtime: 28 ms
# memory: 13.8 MB

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, w in enumerate(words):
            if w.startswith(searchWord):
                return i + 1
        return -1