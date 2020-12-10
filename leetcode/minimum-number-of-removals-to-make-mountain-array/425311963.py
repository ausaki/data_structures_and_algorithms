# title: minimum-number-of-removals-to-make-mountain-array
# detail: https://leetcode.com/submissions/detail/425311963/
# datetime: Sun Nov 29 17:08:14 2020
# runtime: 424 ms
# memory: 14.6 MB

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def LIS(reverse=False):
            lis = []
            stack = []
            rng = range(n) if not reverse else reversed(range(n))
            for i in rng:
                k = 0
                for j in range(len(stack) - 1, -1, -1):
                    if nums[i] > nums[stack[j]]:
                        k = j + 1
                        break
                if k >= len(stack):
                    stack.append(i)
                else:
                    stack[k] = i
                lis.append(k + 1)
            return lis
        
        n = len(nums)
        lis1 = LIS()
        lis2 = LIS(True)
        # print(lis1)
        # print(lis2[::-1])
        return min(n - (lis1[i] + lis2[n - 1 - i] - 1) if lis1[i] > 1 and lis2[n - 1 - i] > 1 else n for i in range(n))
            
        