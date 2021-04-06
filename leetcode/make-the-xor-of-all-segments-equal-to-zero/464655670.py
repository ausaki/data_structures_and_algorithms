# title: make-the-xor-of-all-segments-equal-to-zero
# detail: https://leetcode.com/submissions/detail/464655670/
# datetime: Sun Mar  7 17:54:10 2021
# runtime: 5404 ms
# memory: 15 MB

class Solution:
    '''
    仔细观察每个长度为 k 的序列的异或的情况, 会发现这么一个规律: 每个连续的长度为 k 的序列是相同的.
    nums[:k] == nums[k: 2 * k] == nums[2 * k: 3 * k] == nums[3 * k: 4 * k] ...
    
    nums[0], nums[1], ... nums[k]
    nums[k], nums[k + 1], ... nums[2 * k - 1]
    nums[2 * k], nums[2 * k + 1], ... nums[3 * k - 1]
    ...
    
    因此, 题目就转换为: 如何使改变的元素最少, 从而每个序列都相等而且序列的异或值等于 0.
    
    先假设不要求序列的异或值等于 0, 则在从 0 - k 的每个位置, 我们可以选择出现次数最多的那个元素.
    '''
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [collections.Counter() for i in range(k)]
        for i, j in enumerate(nums):
            cnt[i % k][j] += 1
        max_freqs = [max(c.values()) for c in cnt]
        res = n - sum(max_freqs) + min(max_freqs)
        M = (1 << 10)
        dp = [-n] * M
        dp[0] = 0
        for i in range(k):
            dp = [max(dp[xor ^ x] + v for x, v in cnt[i].items()) for xor in range(M)]
        return min(res, n - dp[0])
    
    