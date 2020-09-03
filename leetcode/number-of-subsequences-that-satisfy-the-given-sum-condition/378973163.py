# title: number-of-subsequences-that-satisfy-the-given-sum-condition
# detail: https://leetcode.com/submissions/detail/378973163/
# datetime: Tue Aug 11 02:20:53 2020
# runtime: 716 ms
# memory: 25.2 MB

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        M=len(nums)
        right=M-1
        ans=0
        Z=10**9+7
        dp=M*[1]
        for i in range(1,M):
            dp[i]=(dp[i-1]*2)%Z
        for left in range(M):
            if 2*nums[left]>target:
                return ans
            else:
                while right>left:
                    if nums[left]+nums[right]>target:
                        right-=1
                    else:
                        break
            ans+=dp[right-left]
            ans=ans%Z
        return ans