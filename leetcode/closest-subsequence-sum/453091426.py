# title: closest-subsequence-sum
# detail: https://leetcode.com/submissions/detail/453091426/
# datetime: Sun Feb  7 14:22:10 2021
# runtime: 1856 ms
# memory: 177.6 MB

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        neg = [i for i in nums if i < 0]
        pos = [i for i in nums if i > 0]
        mi, ma = sum(neg), sum(pos)
        if goal <= mi:
            return mi - goal
        if goal >= ma:
            return goal - ma
        
        n = len(nums)
        m = n // 2
        prev_code = 0
        prev_sum = 0
        left = {0}
        for i in range(1, 1 << m):
            g = i ^ (i >> 1)
            k = (g ^ prev_code) 
            prev_code = g
            if g & k:
                prev_sum += nums[k.bit_length() - 1]
            else:
                prev_sum -= nums[k.bit_length() - 1]
            left.add(prev_sum)
                
        right = {0}
        prev_code, prev_sum = 0, 0
        for i in range(1, (1 << (n - m))):
            g = i ^ (i >> 1)
            k = (g ^ prev_code) 
            prev_code = g
            if g & k:
                prev_sum += nums[m + k.bit_length() - 1]
            else:
                prev_sum -= nums[m + k.bit_length() - 1]
            right.add(prev_sum)
            
        # print(left, right)
        res = math.inf
        right = sorted(right)
        for i in left:
            j = bisect.bisect(right, goal - i)
            res = min(res, abs(goal - (right[j] + i)) if j < len(right) else math.inf, 
                            abs(goal - (right[j - 1] + i)) if j else math.inf)
        return res
        
            
        
        