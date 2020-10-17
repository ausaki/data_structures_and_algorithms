# title: goat-latin
# detail: https://leetcode.com/submissions/detail/409002602/
# datetime: Thu Oct 15 17:19:40 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        result = []
        for i, w in enumerate(words, 1):
            if w[0].lower() in 'aeiou':
                result.append(w + 'ma' + 'a' * i)
            else:
                result.append(w[1:] + w[0] + 'ma' + 'a' * i)
        return ' '.join(result)