# title: find-two-non-overlapping-sub-arrays-each-with-target-sum
# detail: https://leetcode.com/submissions/detail/380824512/
# datetime: Fri Aug 14 23:19:28 2020
# runtime: 1136 ms
# memory: 46.8 MB

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sum = {0: -1}
        stack = []
        suffix_sum = {0: n}
        curr = 0
        for i, a in enumerate(arr):
            curr += a
            diff = curr - target
            if diff in prefix_sum:
                l = i - prefix_sum[diff]
                if not stack or l < stack[-1][0]:
                    stack.append((l, i))
            prefix_sum[curr] = i
        curr = 0
        l2 = n
        result = n + 1
        for i in range(n - 1, -1, -1):
            curr += arr[i]
            diff = curr - target
            if diff in suffix_sum:
                l2 = min(l2, suffix_sum[diff] - i)
            suffix_sum[curr] = i
            if stack and stack[-1][1] >= i:
                stack.pop()
            if not stack:
                break
            l1 = stack[-1][0]
            result = min(result, l1 + l2)
        return result if result < n + 1 else -1