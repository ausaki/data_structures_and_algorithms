# title: determine-if-string-halves-are-alike
# detail: https://leetcode.com/submissions/detail/434970150/
# datetime: Sun Dec 27 10:34:06 2020
# runtime: 40 ms
# memory: 14.3 MB

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = collections.Counter(s[:len(s) // 2]), collections.Counter(s[len(s) // 2:])
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        return sum(a[v] for v in vowels) == sum(b[v] for v in vowels)
        