# title: similar-string-groups
# detail: https://leetcode.com/submissions/detail/408666084/
# datetime: Wed Oct 14 23:06:33 2020
# runtime: 580 ms
# memory: 14.8 MB

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
        def check(X, Y):
            diff = 0
            for x, y in zip(X, Y):
                if x != y:
                    diff += 1
                if diff > 2:
                    return False
            return True
        
        A = list(set(A))
        m, n = len(A), len(A[0])
        dj = DisjSet(m)
        blocks = collections.defaultdict(list)
        if n >= 6:
            for i, word in enumerate(A):
                step = n // 3
                for j in range(0, step * 3, step):
                    blocks[word[j:j + step] + str(j)].append(i)
        else:
            blocks['all'] = range(m)
        for idx in blocks.values():
            for i, j in itertools.combinations(idx, 2):
                if check(A[i], A[j]):
                    dj.union(i, j)
        return sum(1 for i in dj.disj_set if i < 0)