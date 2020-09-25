# title: decrease-elements-to-make-array-zigzag
# detail: https://leetcode.com/submissions/detail/396663851/
# datetime: Thu Sep 17 01:54:40 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        nums.insert(0, 2000)
        nums.append(2000)
        n = len(nums)
        cnt = [0, 0]
        for i in range(1, n - 1):
            if not ((nums[i] < nums[i - 1]) and (nums[i] < nums[i + 1])):
                cnt[i % 2] += 1 + nums[i] - min(nums[i - 1], nums[i + 1])
        return min(cnt)
        
        