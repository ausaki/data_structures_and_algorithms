# title: circular-array-loop
# detail: https://leetcode.com/submissions/detail/281598150/
# datetime: Tue Nov 26 00:44:29 2019
# runtime: 48 ms
# memory: 12.9 MB

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 0:
            return False
        i = 0
        direction = nums[i]
        step = 0
        mark = 2000
        base = 2000
        while True:
            if step == 0:
                if nums[i] >= mark:
                    j = (i + 1) % N
                    while j != i and nums[j] >= mark:
                        j = (j + 1) % N
                    if j == i:
                        break
                    i = j
                direction = nums[i]
                j = (i + nums[i]) % N
                nums[i] = base 
                i = j
                step = 1
                continue
            if nums[i] >= base and step - (nums[i] - base) > 1:
                return True
            if nums[i] >= mark:
                base += step
                step = 0
                continue
            if (direction ^ nums[i]) >= 0:
                j = (i + nums[i]) % N
                nums[i] = base + step
                i = j
                step += 1
            else:
                base += step
                step = 0
        return False