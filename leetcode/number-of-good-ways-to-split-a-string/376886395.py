# title: number-of-good-ways-to-split-a-string
# detail: https://leetcode.com/submissions/detail/376886395/
# datetime: Thu Aug  6 16:15:58 2020
# runtime: 264 ms
# memory: 14.6 MB

class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right_counter = collections.Counter(s)
        right = set(right_counter)
        result = 0
        for i in range(len(s) - 1):
            left.add(s[i])
            right_counter[s[i]] -= 1
            if right_counter[s[i]] == 0:
                right.remove(s[i])
            if len(left) == len(right):
                result += 1
        return result