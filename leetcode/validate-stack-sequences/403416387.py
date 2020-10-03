# title: validate-stack-sequences
# detail: https://leetcode.com/submissions/detail/403416387/
# datetime: Fri Oct  2 14:25:52 2020
# runtime: 116 ms
# memory: 14.3 MB

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j, k, n = -1, 0, 0, len(pushed)
        while i < n and k < n:
            if i >= 0 and pushed[i] == popped[k]:
                i -= 1
                k += 1
            else:
                if j >= n:
                    break
                i += 1
                pushed[i] = pushed[j]
                j += 1
        return i == -1 and k == n