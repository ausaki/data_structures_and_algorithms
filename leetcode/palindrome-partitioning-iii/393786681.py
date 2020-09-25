# title: palindrome-partitioning-iii
# detail: https://leetcode.com/submissions/detail/393786681/
# datetime: Thu Sep 10 23:43:34 2020
# runtime: 344 ms
# memory: 14 MB

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        
        def cost(s,i,j): #calculate the cost of transferring one substring into palindrome string
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r
        
        def dfs(i, k):
            if (i, k) in memo: return memo[(i, k)] #case already in memo
            if n - i == k: #base case that each substring just have one character
                return 0
            if k == 1:    #base case that need to transfer whole substring into palidrome
                return cost(s, i, n - 1)
            res = float('inf')
            for j in range(i + 1, n - k + 2): # keep making next part of substring into palidrome
                res = min(res, dfs(j, k - 1) + cost(s,i, j - 1)) #compare different divisions to get the minimum cost
            memo[(i, k)] = res
            return res
        return dfs(0 , k)