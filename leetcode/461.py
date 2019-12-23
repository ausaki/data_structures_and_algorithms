# from functools import lru_cache
class Solution:
    def canPartition(self, nums):
        cache = {}
        def find(i, target):
            # print(i, target)
            if i in cache and target in cache[i]:
                return cache[i][target]
            v = False
            if target == 0:
                v = True
            elif i < 0 or target < 0:
                v = False
            else:
                for j in range(i, -1, -1):
                    if find(j - 1, target - nums[j]):
                        v = True
                        break
            if i not in cache:
                cache[i] = {}
            cache[i][target] = v
            return v
        N = len(nums)
        S = sum(nums)
        if S % 2:
            return False
        nums.sort()
        res = find(N - 1, S // 2)
        print(len(cache), cache.keys())
        return res


testcase = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]

Solution().canPartition(testcase)

