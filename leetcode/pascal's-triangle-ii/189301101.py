# title: pascal's-triangle-ii
# detail: https://leetcode.com/submissions/detail/189301101/
# datetime: Tue Nov 13 17:47:08 2018
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
                if j == 0:
                    v = 1
                else:
                    v = nums[j - 1] + nums[j]
                nums[j] = v
                nums[i - j] = v
        return nums
        