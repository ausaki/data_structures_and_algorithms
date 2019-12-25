# title: longest-word-in-dictionary-through-deleting
# detail: https://leetcode.com/submissions/detail/286613206/
# datetime: Tue Dec 17 18:54:00 2019
# runtime: 460 ms
# memory: 14.7 MB

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def match(word):
            i = 0
            j = len(word) - 1
            m = 0
            n = len(s) - 1
            while i <= j and m <= n:
                while i <= j and m <= n and s[m] != word[i]:
                    m += 1
                if m <= n:
                    i += 1
                    m += 1
                while i <= j and m <= n and s[n] != word[j]:
                    n -= 1
                if m <= n:
                    j -= 1
                    n -= 1
            return i > j
                
        res = ''
        for word in d:
            l = len(word)
            if l > len(s) or l < len(res): 
                continue
            if match(word) and (l > len(res) or word < res):
                res = word
        return res