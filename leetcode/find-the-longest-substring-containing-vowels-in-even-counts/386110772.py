# title: find-the-longest-substring-containing-vowels-in-even-counts
# detail: https://leetcode.com/submissions/detail/386110772/
# datetime: Tue Aug 25 18:22:44 2020
# runtime: 168 ms
# memory: 19.7 MB

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        dp = {}
        for k in range(n, 0, -1):
            for i in range(0, n + 1 - k):
                if k == n:
                    s_count = collections.Counter(s)
                    dp[(i, k)] = [s_count.get(c, 0) % 2 == 0 for c in 'aeiou']
                elif i == 0:
                    dp[(i, k)] = self.update_tracker(s[i + k], dp.get((i, k + 1)))
                else:
                    dp[(i, k)] = self.update_tracker(s[i - 1], dp.get((i - 1, k + 1)))
                if all(dp[(i, k)]):
                    return k
        return 0
                
        
    def update_tracker(self, char, tracker):
        idx = 'aeiou'.find(char)
        new_tracker = list(tracker)
        if idx > -1:
            new_tracker[idx] = not tracker[idx]
        return new_tracker