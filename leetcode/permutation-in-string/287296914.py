# title: permutation-in-string
# detail: https://leetcode.com/submissions/detail/287296914/
# datetime: Fri Dec 20 15:38:26 2019
# runtime: 64 ms
# memory: 12.8 MB

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N1, N2 = len(s1), len(s2) 
        if N1 > N2: return False
        s1_cnt = collections.Counter(s1)
        left = 0
        right = len(s1) - 1
        window_cnt = collections.Counter(s2[left: right])
        while right < N2:
            window_cnt[s2[right]] += 1
            if s1_cnt == window_cnt:
                return True
            window_cnt[s2[left]] -= 1
            if window_cnt[s2[left]] == 0:
                window_cnt.pop(s2[left])
            left += 1
            right += 1
        return False