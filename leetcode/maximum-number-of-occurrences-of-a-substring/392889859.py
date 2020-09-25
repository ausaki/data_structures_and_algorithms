# title: maximum-number-of-occurrences-of-a-substring
# detail: https://leetcode.com/submissions/detail/392889859/
# datetime: Wed Sep  9 01:25:13 2020
# runtime: 280 ms
# memory: 15.8 MB

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        s0 = s[:minSize]
        counter = collections.Counter(s0)
        substr = collections.Counter()
        if len(counter) <= maxLetters:
            substr[s0] += 1
        for i in range(minSize, n):
            l = i - minSize
            counter[s[i - minSize]] -= 1
            counter[s[i]] += 1
            if counter[s[i - minSize]] == 0:
                counter.pop(s[i - minSize])
            if len(counter) <= maxLetters:
                substr[s[i - minSize + 1: i + 1]] += 1
        return max(substr.values(), default=0)