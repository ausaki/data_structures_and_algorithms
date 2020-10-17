# title: goat-latin
# detail: https://leetcode.com/submissions/detail/409003108/
# datetime: Thu Oct 15 17:22:16 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        return ' '.join((w if w[0].lower() in 'aeiou' else w[1:] + w[0]) + 'ma' + 'a' * i for i, w in enumerate(S.split(), 1))
