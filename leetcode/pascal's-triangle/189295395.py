# title: pascal's-triangle
# detail: https://leetcode.com/submissions/detail/189295395/
# datetime: Tue Nov 13 16:56:56 2018
# runtime: 28 ms
# memory: N/A

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        result = [[1]]
        for i in range(1, numRows):
            prev_nums = result[i - 1]
            nums = []
            result.append(nums)
            
            for j in range(i + 1):
                if j == 0 or j == i:
                    nums.append(1)
                else:
                    nums.append(prev_nums[j - 1] + prev_nums[j])
            
        return result
            
            
            
        