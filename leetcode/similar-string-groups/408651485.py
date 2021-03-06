# title: similar-string-groups
# detail: https://leetcode.com/submissions/detail/408651485/
# datetime: Wed Oct 14 22:16:24 2020
# runtime: 7192 ms
# memory: 75.7 MB

class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        
    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        dj = DisjSet(m)
        if m < n * n:
            for i in range(m):
                for j in range(i):
                    diff = sum(1 for x, y in zip(A[i], A[j]) if x != y)
                    if diff <= 2:
                        dj.union(i, j)
        else:
            words = collections.defaultdict(list)
            for i, word in enumerate(A):
                for j, k in itertools.combinations(range(n), 2):
                    w = word[:j] + '*' + word[j + 1:k] + '*' + word[k + 1:]
                    words[w].append(i)
                    dj.union(words[w][0], i)
        return sum(1 for i in dj.disj_set if i < 0)