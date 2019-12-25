# title: find-all-anagrams-in-a-string
# detail: https://leetcode.com/submissions/detail/285876186/
# datetime: Sat Dec 14 20:28:14 2019
# runtime: 136 ms
# memory: 13.7 MB

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        M = len(p)
        if N == 0 or len(p) == 0 or len(p) > N:
            return []
        p_counter = collections.Counter(p)
        left = 0
        right = M - 1
        counter = collections.Counter(s[left:right])
        res = []
        while right < N:
            counter[s[right]] += 1
            # print(left, right, counter)
            if counter == p_counter:
                res.append(left)            
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                counter.pop(s[left])
            left += 1
            right += 1      
        return res
