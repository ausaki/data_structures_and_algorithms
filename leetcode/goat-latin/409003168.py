# title: goat-latin
# detail: https://leetcode.com/submissions/detail/409003168/
# datetime: Thu Oct 15 17:22:31 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def toGoatLatin(self, S: str) -> str:
        return ' '.join((w if w[0].lower() in 'aeiou' else w[1:] + w[0]) + 'ma' + 'a' * i for i, w in enumerate(S.split(), 1))
