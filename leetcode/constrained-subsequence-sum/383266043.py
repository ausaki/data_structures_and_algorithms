# title: constrained-subsequence-sum
# detail: https://leetcode.com/submissions/detail/383266043/
# datetime: Wed Aug 19 23:59:30 2020
# runtime: 544 ms
# memory: 27 MB

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = collections.deque([(nums[0], 0)])
        result = nums[0]
        for i in range(1, n):
            while q and q[0][1] < i - k:
                q.popleft()
            a = q[0][0]
            m = nums[i] + (a if a > 0 else 0)
            while q and m >= q[-1][0]:
                q.pop()
            q.append((m, i))
            result = max(result, m)
        return result