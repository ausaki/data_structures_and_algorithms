# title: accounts-merge
# detail: https://leetcode.com/submissions/detail/288708015/
# datetime: Thu Dec 26 22:42:39 2019
# runtime: 208 ms
# memory: 16.2 MB

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
        if j == -1:
            return
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
    def sets(self):
        res = {}
        for i, j in self.elements.items():
            k = self.find(j)
            if k not in res:
                res[k] = []
            res[k].append(i)
        return res
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mapping = {}
        disj = DisjSet()
        for i, account in enumerate(accounts):
            disj.add(i)
            name = account[0]
            for j in range(1, len(account)):
                if account[j] in mapping:
                    disj.union(i, mapping[account[j]])
                else:
                    mapping[account[j]] = i
        res = []
        for i, sets in disj.sets().items():
            name = accounts[sets[0]][0]
            emails = set()
            for j in sets:
                emails |= set(accounts[j][1:])
            res.append([name] + sorted(emails))
        return res