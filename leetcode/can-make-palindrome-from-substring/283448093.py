# title: can-make-palindrome-from-substring
# detail: https://leetcode.com/submissions/detail/283448093/
# datetime: Tue Dec  3 22:20:00 2019
# runtime: 1724 ms
# memory: 59.9 MB

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        enc = lambda ch: 1 << (ord(ch) - ord('a'))
        cache = [None] * len(s)
        cache[0] = enc(s[0])
        for i in range(1, len(s)):
            cache[i] = enc(s[i]) ^ cache[i - 1]
        # print(cache)
        def query(l, r, k):
            i = cache[r]
            j = cache[l - 1] if l > 0 else 0
            i = i ^ j
            cnt = 0
            while i:
                cnt += 1
                i &= i - 1
            return (cnt // 2) <= k
        
        answer = [query(*q) for q in queries]
        return answer