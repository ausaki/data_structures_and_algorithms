# title: maximum-product-of-word-lengths
# detail: https://leetcode.com/submissions/detail/279281911/
# datetime: Sun Nov 17 01:17:45 2019
# runtime: 424 ms
# memory: 13 MB

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        encodings = []
        for w in words:
            n = 0
            for c in w:
                n |= 1 << (ord(c) - ord('a'))
            encodings.append(n)
        result = 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                if encodings[i] & encodings[j] == 0:
                    r = len(words[i]) * len(words[j])
                    if r > result:
                        result = r
        return result                
        