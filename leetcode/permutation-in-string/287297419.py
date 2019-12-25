# title: permutation-in-string
# detail: https://leetcode.com/submissions/detail/287297419/
# datetime: Fri Dec 20 15:41:28 2019
# runtime: 56 ms
# memory: 12.8 MB

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N1, N2 = len(s1), len(s2) 
        if N1 > N2: return False
        s1_cnt = [0] * 26
        for c in s1:
            s1_cnt[ord(c) - ord('a')] += 1
        left = 0
        right = len(s1) - 1
        window_cnt = [0] * 26
        for c in s2[left:right]:
            window_cnt[ord(c) - ord('a')] += 1
        while right < N2:
            window_cnt[ord(s2[right]) - ord('a')] += 1
            if s1_cnt == window_cnt:
                return True
            window_cnt[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
        return False