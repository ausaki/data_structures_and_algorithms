# title: longest-substring-with-at-least-k-repeating-characters
# detail: https://leetcode.com/submissions/detail/285429753/
# datetime: Thu Dec 12 14:46:26 2019
# runtime: 36 ms
# memory: 13 MB

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def find(left, right):
            # print(left, right)
            if left == right:
                return 1 if k <= 1 else 0
            if left > right:
                return 0
            counter = {}
            for i in range(left, right + 1):
                char = s[i]
                if char not in counter:
                    counter[char] = []
                counter[char].append(i)
            blacklist = []
            for char, index in counter.items():
                if len(index) < k:
                    blacklist.extend(index)
            blacklist.sort()
            if not blacklist:
                return right - left + 1
            blacklist.append(right + 1)
            res = 0
            for i in blacklist:
                res = max(res, find(left, i - 1))
                left = i + 1
            return res
        
        N = len(s)
        if N == 0:
            return 0
        return find(0, N - 1)