# title: find-all-anagrams-in-a-string
# detail: https://leetcode.com/submissions/detail/285876561/
# datetime: Sat Dec 14 20:32:16 2019
# runtime: 96 ms
# memory: 13.6 MB

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        M = len(p)
        if N == 0 or len(p) == 0 or len(p) > N:
            return []
        p_counter = [0] * 26
        for char in p:
            p_counter[ord(char) - ord('a')] += 1
        left = 0
        right = M - 1
        counter = [0] * 26
        for i in range(left, right):
            counter[ord(s[i]) - ord('a')] += 1
        res = []
        while right < N:
            counter[ord(s[right]) - ord('a')] += 1
            # print(left, right, counter)
            if counter == p_counter:
                res.append(left)            
            counter[ord(s[left]) - ord('a')] -= 1
            left += 1
            right += 1      
        return res
