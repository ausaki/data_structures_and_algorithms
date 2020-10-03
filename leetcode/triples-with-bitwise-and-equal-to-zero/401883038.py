# title: triples-with-bitwise-and-equal-to-zero
# detail: https://leetcode.com/submissions/detail/401883038/
# datetime: Tue Sep 29 01:21:39 2020
# runtime: 5128 ms
# memory: 19 MB

class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        cnt = collections.Counter()
        A = list(collections.Counter(A).items())
        result = 0
        for i, k1 in A:
            for j, k2 in A:
                cnt[i & j] += k1 * k2
        cnt = list(cnt.items())
        for i, k1 in A:
            if i == 0:
                result += k1 * n * n
                continue
            for j, k2 in cnt:
                if i & j == 0:
                    result += k1 * k2
        return result