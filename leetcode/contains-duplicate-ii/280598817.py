# title: contains-duplicate-ii
# detail: https://leetcode.com/submissions/detail/280598817/
# datetime: Thu Nov 21 19:48:28 2019
# runtime: 140 ms
# memory: 19.3 MB

from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        N = len(nums)
        cnt = Counter(nums[1: 1 + k])
        for i in range(N - 1):
            if nums[i] in cnt:
                return True
            key = nums[i + 1]
            cnt[key] -= 1
            if cnt[key] == 0:
                cnt.pop(key)
            if i + 1 + k < N:
                cnt[nums[i + 1 + k]] += 1
        return False