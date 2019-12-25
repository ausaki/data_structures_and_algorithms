# title: pascal's-triangle-ii
# detail: https://leetcode.com/submissions/detail/189299577/
# datetime: Tue Nov 13 17:33:02 2018
# runtime: 24 ms
# memory: N/A

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[1]]
        for i in range(1, rowIndex + 1):
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
        return result[-1]
        