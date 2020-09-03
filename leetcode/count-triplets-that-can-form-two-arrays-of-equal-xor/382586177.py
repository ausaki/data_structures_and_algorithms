# title: count-triplets-that-can-form-two-arrays-of-equal-xor
# detail: https://leetcode.com/submissions/detail/382586177/
# datetime: Tue Aug 18 14:46:16 2020
# runtime: 40 ms
# memory: 13.9 MB

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prev_xor = {0: [-1]}
        curr = 0
        result = 0
        for i, a in enumerate(arr):
            curr ^= a
            if curr in prev_xor:
                for j in prev_xor[curr]:
                    result += i - j - 1
            else:
                prev_xor[curr] = []
            prev_xor[curr].append(i)
        return result