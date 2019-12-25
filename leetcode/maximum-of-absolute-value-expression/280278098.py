# title: maximum-of-absolute-value-expression
# detail: https://leetcode.com/submissions/detail/280278098/
# datetime: Wed Nov 20 14:03:08 2019
# runtime: 348 ms
# memory: 19.5 MB

from operator import add, sub

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max_values = [0] * 4
        min_values = [0] * 4
        operators = [[add, add], [add, sub], [sub, add], [sub, sub]]
        for j, [op1, op2] in enumerate(operators):
            min_values[j] = max_values[j] = op2(op1(arr1[0], arr2[0]), 0)
            
        for i in range(1, len(arr1)):
            for j, [op1, op2] in enumerate(operators):
                v = op2(op1(arr1[i], arr2[i]), i)
                if v > max_values[j]:
                    max_values[j] = v
                if v < min_values[j]:
                    min_values[j] = v
        return max(max_values[i] - min_values[i] for i in range(4))
             