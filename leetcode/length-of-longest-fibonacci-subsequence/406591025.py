# title: length-of-longest-fibonacci-subsequence
# detail: https://leetcode.com/submissions/detail/406591025/
# datetime: Fri Oct  9 23:28:00 2020
# runtime: 648 ms
# memory: 14.3 MB

class Solution(object):
    def lenLongestFibSubseq(self, A):
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0