# title: rearrange-words-in-a-sentence
# detail: https://leetcode.com/submissions/detail/382053340/
# datetime: Mon Aug 17 12:39:25 2020
# runtime: 36 ms
# memory: 15.5 MB

class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()
        words.sort(key=lambda w: len(w))
        return ' '.join(words).capitalize()
