# title: satisfiability-of-equality-equations
# detail: https://leetcode.com/submissions/detail/401746743/
# datetime: Mon Sep 28 16:41:04 2020
# runtime: 52 ms
# memory: 14.2 MB

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
    def equationsPossible(self, equations: List[str]) -> bool:
        d = DisjSet(26)
        for eq in equations:
            a, b = ord(eq[0]) - 97, ord(eq[3]) - 97
            if eq[1] == '=':
                d.union(a, b)
        for eq in equations:
            if eq[1] == '!':
                a, b = ord(eq[0]) - 97, ord(eq[3]) - 97
                if d.find(a) == d.find(b):
                    return False
        return True
            