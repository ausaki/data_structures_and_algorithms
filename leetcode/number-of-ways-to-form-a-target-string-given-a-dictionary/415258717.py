# title: number-of-ways-to-form-a-target-string-given-a-dictionary
# detail: https://leetcode.com/submissions/detail/415258717/
# datetime: Sun Nov  1 00:14:20 2020
# runtime: 3036 ms
# memory: 356 MB

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        wl,tl=len(words[0]),len(target)
        if wl<tl:
            return 0
        lookup=collections.defaultdict(int) # lookup[i,j]=#of word in words such that word[i]==target[j]
        cnts=[]
        for i in range(wl):
            cnts.append(collections.Counter([wd[i] for wd in words]))
        for j in range(tl):
            for i in range(wl):
                lookup[i,j]=cnts[i][target[j]]
        memo={}
        mod=10**9+7
        def helper(i,j):
            # num of ways for [wd[i:] for wd in words] to formulate target[j:]
            if j<i-wl+tl or i>=wl:
                return 0
            if (i,j) in memo:
                return memo[i,j]
            if j==tl-1:
                ans=(lookup[i,j]+helper(i+1,j))%mod
            else:
                ans=helper(i+1,j)
                ans+=lookup[i,j]*helper(i+1,j+1)
                ans=ans%mod
            memo[i,j]=ans
            return ans
        return helper(0,0)
            