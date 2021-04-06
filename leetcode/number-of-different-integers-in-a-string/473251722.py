# title: number-of-different-integers-in-a-string
# detail: https://leetcode.com/submissions/detail/473251722/
# datetime: Sun Mar 28 10:38:41 2021
# runtime: 36 ms
# memory: 14.1 MB

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        i = -1
        ints = set()
        for j, c in enumerate(word):
            if c.isdigit():
                if i == -1:
                    i = j
            else:
                if i != -1:
                    ints.add(int(word[i:j]))
                i = -1
        if i != -1:
            ints.add(int(word[i:]))
        
        return len(ints)