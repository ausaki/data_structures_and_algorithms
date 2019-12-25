# title: friend-circles
# detail: https://leetcode.com/submissions/detail/286881863/
# datetime: Wed Dec 18 22:27:44 2019
# runtime: 224 ms
# memory: 12.9 MB

class DisjSet:
    def __init__(self):
        self.elements = {}
        self.disj_set = []

    def add(self, x):
        if x not in self.elements:
            self.elements[x] = len(self.disj_set)
            self.disj_set.append(-1)

    def find(self, x):
        if x not in self.elements:
            return -1
        i = self.elements[x]
        while self.disj_set[i] >= 0:
            i = self.disj_set[i]
        return i

    def union(self, x, y):
        i = self.find(x)
        if i == -1:
            return
        j = self.find(y)
        if j == -1 or j == i:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j

    def count_set(self):
        count = 0
        for i in self.disj_set:
            if i < 0:
                count += 1
        return count

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        disjset = DisjSet()
        
        for i in range(len(M)):
            disjset.add(i)
        for i in range(len(M)):
            for j in range(len(M)):
                if i == j:
                    continue
                if M[i][j] == 1:
                    disjset.union(i, j)
        return disjset.count_set()