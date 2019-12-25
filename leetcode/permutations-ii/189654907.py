# title: permutations-ii
# detail: https://leetcode.com/submissions/detail/189654907/
# datetime: Thu Nov 15 11:24:43 2018
# runtime: 76 ms
# memory: N/A

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        pool = sorted(nums)
        n = len(pool)
        r = n
        indices = list(range(r))
        reversed_indices = list(reversed(range(r)))
        cycles = list(range(n, n-r, -1))
        result.append(list(pool[i] for i in indices))
        while n:
            for i in reversed_indices:
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    while pool[indices[i]] == pool[indices[-j]] and j > 0:
                        j -= 1
                    if j > 0:
                        cycles[i] = j
                        indices[i], indices[-j] = indices[-j], indices[i]
                        result.append(list(pool[i] for i in indices[:r]))
                        break
                    else:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = n - i
            else:
                return result