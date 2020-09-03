# title: count-triplets-that-can-form-two-arrays-of-equal-xor
# detail: https://leetcode.com/submissions/detail/382595516/
# datetime: Tue Aug 18 15:12:28 2020
# runtime: 36 ms
# memory: 13.7 MB

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prev_xor = {0: [-1, 0, 1]}
        curr = 0
        result = 0
        for i, a in enumerate(arr):
            curr ^= a
            if curr in prev_xor:
                j, k, l = prev_xor[curr]
                cnt = k + (i - j) * l - 1
                result += cnt
                prev_xor[curr][0] = i
                prev_xor[curr][1] = cnt
                prev_xor[curr][2] += 1
            else:
                prev_xor[curr] = [i, 0, 1]
        return result