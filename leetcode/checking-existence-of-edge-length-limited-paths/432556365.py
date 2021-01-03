# title: checking-existence-of-edge-length-limited-paths
# detail: https://leetcode.com/submissions/detail/432556365/
# datetime: Sun Dec 20 16:26:17 2020
# runtime: 1992 ms
# memory: 60.3 MB

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
            return i
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
            return i
        if self.disj_set[i] == self.disj_set[j]:
            self.disj_set[j] -= 1
        self.disj_set[i] = j
        return j
    
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        比赛期间没有想出算法, 感觉好像只要隔一段时间不刷题, 脑子就会变迟钝, 不能第一时间想出正确的算法.
        
        题目中要求找出两个顶点之间是否存在一条路径, 上面的每条边的长度都小于 limit.
        
        这其实有点障眼法, 换个角度看, 可以认为长度大于等于 limit 的边是断开的, 可以将其从图中删除.
        如果只要求找出一对顶点之间是否存在符合要求的路径, 那么使用 UnionFind 就可以了.
        可是题目给出了一系列的顶点对, 思路是将 queries 按照 limit 排序(递增), 接着在遍历 queries 的过程中, 不断往 UnionFind 结构添加边.
        '''

        ds = DisjSet(n)
        idx = list(range(len(queries)))
        idx.sort(key=lambda i: queries[i][2])
        edgeList.sort(key=lambda e: e[2])
        m = len(edgeList)
        i = 0
        res = [False] * len(queries)
        for k in idx:
            for i in range(i, m):
                if edgeList[i][2] < queries[k][2]:
                    ds.union(edgeList[i][0], edgeList[i][1])
                else:
                    break
            res[k] = ds.find(queries[k][0]) == ds.find(queries[k][1])
        return res
                
        