# title: find-the-duplicate-number
# detail: https://leetcode.com/submissions/detail/284560068/
# datetime: Sun Dec  8 22:54:25 2019
# runtime: 64 ms
# memory: 15.1 MB

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow        