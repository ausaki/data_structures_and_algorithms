# title: rearrange-words-in-a-sentence
# detail: https://leetcode.com/submissions/detail/382052399/
# datetime: Mon Aug 17 12:37:03 2020
# runtime: 60 ms
# memory: 17.1 MB

class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0][0].lower() + words[0][1:]
        words.sort(key=lambda w: (len(w), ))
        new_words = sorted(zip(words, range(len(words))), key=lambda item: (len(item[0]), item[1]))
        t = ' '.join(w for w, _ in new_words)
        return t[0].upper() + t[1:]