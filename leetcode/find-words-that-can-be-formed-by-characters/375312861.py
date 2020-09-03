# title: find-words-that-can-be-formed-by-characters
# detail: https://leetcode.com/submissions/detail/375312861/
# datetime: Mon Aug  3 15:19:19 2020
# runtime: 176 ms
# memory: 14.2 MB

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = collections.Counter(chars)
        result = 0
        for word in words:
            c = collections.Counter(word)
            l = len(word)
            for i, j in c.items():
                if cnt.get(i, 0) < j:
                    break
            else:
                result += l
        return result