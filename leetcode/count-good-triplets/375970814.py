# title: count-good-triplets
# detail: https://leetcode.com/submissions/detail/375970814/
# datetime: Tue Aug  4 22:45:28 2020
# runtime: 848 ms
# memory: 13.5 MB

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        result = 0
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        result += 1
        return result