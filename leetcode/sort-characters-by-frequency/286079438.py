# title: sort-characters-by-frequency
# detail: https://leetcode.com/submissions/detail/286079438/
# datetime: Sun Dec 15 14:43:48 2019
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = sorted(collections.Counter(s).items(), key=lambda item: item[1], reverse=True)
        return ''.join([item[0] * item[1] for item in freqs])