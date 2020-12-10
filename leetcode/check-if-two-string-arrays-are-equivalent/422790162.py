# title: check-if-two-string-arrays-are-equivalent
# detail: https://leetcode.com/submissions/detail/422790162/
# datetime: Sun Nov 22 10:34:26 2020
# runtime: 36 ms
# memory: 14.5 MB

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(a == b for a, b in itertools.zip_longest(itertools.chain(*word1), itertools.chain(*word2)))