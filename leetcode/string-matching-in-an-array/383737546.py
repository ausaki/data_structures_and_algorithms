# title: string-matching-in-an-array
# detail: https://leetcode.com/submissions/detail/383737546/
# datetime: Thu Aug 20 23:00:43 2020
# runtime: 28 ms
# memory: 14 MB

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        n = len(words)
        result = []
        for i,  word in enumerate(words):
            for j in range(i + 1, n):
                if word in words[j]:
                    result.append(word)
                    break
        return result