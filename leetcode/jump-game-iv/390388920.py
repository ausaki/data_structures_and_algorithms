# title: jump-game-iv
# detail: https://leetcode.com/submissions/detail/390388920/
# datetime: Thu Sep  3 16:30:52 2020
# runtime: 576 ms
# memory: 29.1 MB

class Solution:
    def minJumps(self, A):
        indices = collections.defaultdict(list)
        for i, a in enumerate(A):
            indices[a].append(i)
        done, now = {-1}, {0}
        for steps in itertools.count():
            done |= now
            if len(A) - 1 in done:
                return steps
            now = {j for i in now for j in [i-1, i+1] + indices.pop(A[i], [])} - done