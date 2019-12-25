# title: pascal's-triangle-ii
# detail: https://leetcode.com/submissions/detail/189299725/
# datetime: Tue Nov 13 17:34:31 2018
# runtime: 28 ms
# memory: N/A

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_nums = [1]
        nums = [1]
        for i in range(1, rowIndex + 1):
            nums = [None] * (i + 1)
            
            for j in range(i // 2 + 1):
                if j == 0:
                    v = 1
                else:
                    v = prev_nums[j - 1] + prev_nums[j]
                nums[j] = v
                nums[i - j] = v
            prev_nums = nums
        return nums
        