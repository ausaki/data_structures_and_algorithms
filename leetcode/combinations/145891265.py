# title: combinations
# detail: https://leetcode.com/submissions/detail/145891265/
# datetime: Mon Mar 19 18:44:37 2018
# runtime: 217 ms
# memory: N/A

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        indexes = range(k)
        result.append([_ + 1 for _ in indexes])
        while k < n - indexes[0]:
            for i in reversed(range(k)):
                if k - i < n - indexes[i]:
                    indexes[i] += 1
                    for j in range(i + 1, k):
                        indexes[j] = indexes[j - 1] + 1
                    break
            result.append([_ + 1 for _ in indexes])
        return result
            
                
        