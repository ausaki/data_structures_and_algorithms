# title: number-of-valid-words-for-each-puzzle
# detail: https://leetcode.com/submissions/detail/280324820/
# datetime: Wed Nov 20 18:11:27 2019
# runtime: 556 ms
# memory: 29.5 MB

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def encode(s):
            n = 0
            for c in s:
                n |= 1 << (ord(c) - ord('a'))
            return n
        mapping = {}
        for word in words:
            enc = encode(word)
            mapping[enc] = mapping.get(enc, 0) + 1
                
        result = []
        for puzzle in puzzles:
            first_char = 1 << (ord(puzzle[0]) - ord('a'))
            enc = encode(puzzle)
            count = 0
            n = enc
            while n > 0:
                if (n & first_char) != 0 and n in mapping:
                    count += mapping[n]
                n = enc & (n - 1)
            result.append(count)
        return result
        