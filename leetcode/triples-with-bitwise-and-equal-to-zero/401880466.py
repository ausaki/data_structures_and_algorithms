# title: triples-with-bitwise-and-equal-to-zero
# detail: https://leetcode.com/submissions/detail/401880466/
# datetime: Tue Sep 29 01:13:55 2020
# runtime: 5308 ms
# memory: 17 MB

class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        cnt = collections.Counter()
        result = 0
        for i in A:
            for j in A:
                cnt[i & j] += 1
        for i in A:
            for j, k in cnt.items():
                if i & j == 0:
                    result += k
        return result