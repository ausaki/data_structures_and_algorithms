# title: similar-string-groups
# detail: https://leetcode.com/submissions/detail/408658957/
# datetime: Wed Oct 14 22:42:49 2020
# runtime: 6496 ms
# memory: 53 MB

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
        A = list(set(A))
        m, n = len(A), len(A[0])
        dj = DisjSet(m)
        if m < n * n:
            for i in range(m):
                for j in range(i):
                    diff = sum(1 for x, y in zip(A[i], A[j]) if x != y)
                    if diff <= 2:
                        dj.union(i, j)
        else:
            words = {}
            for i, word in enumerate(A):
                for j, k in itertools.combinations(range(n), 2):
                    w = word[:j] + '*' + word[j + 1:k] + '*' + word[k + 1:]
                    dj.union(words.setdefault(w, i), i)
        return sum(1 for i in dj.disj_set if i < 0)