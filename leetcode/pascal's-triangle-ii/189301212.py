# title: pascal's-triangle-ii
# detail: https://leetcode.com/submissions/detail/189301212/
# datetime: Tue Nov 13 17:48:08 2018
# runtime: 24 ms
# memory: N/A

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nums = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i // 2, 0, -1):
                nums[j] = nums[i - j] = nums[j - 1] + nums[j]
        return nums
        