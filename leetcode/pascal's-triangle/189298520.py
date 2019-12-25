# title: pascal's-triangle
# detail: https://leetcode.com/submissions/detail/189298520/
# datetime: Tue Nov 13 17:22:50 2018
# runtime: 20 ms
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
            nums = [None] * (i + 1)
            
            for j in range(i // 2 + 1):
                if j == 0:
                    v = 1
                else:
                    v = prev_nums[j - 1] + prev_nums[j]
                nums[j] = v
                nums[i - j] = v
                
            result.append(nums)
        return result