# title: tree-of-coprimes
# detail: https://leetcode.com/submissions/detail/458414268/
# datetime: Sun Feb 21 00:22:58 2021
# runtime: 2636 ms
# memory: 117.8 MB

class Solution:
    coprimes = [[0] * 51 for i in range(51)]
    for i in range(1, 51):
        for j in range(1, 51):
            coprimes[i][j] = math.gcd(i, j) == 1
            
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        t = collections.defaultdict(list)
        for a, b in edges:
            t[a].append(b)
            t[b].append(a)
        vals = {}
        
        def visit(i, prev, depth, vals):
            val = nums[i]
            max_depth = -1
            k = -1
            for v, (d, j) in vals.items():
                if self.coprimes[val][v] and d > max_depth:
                    max_depth = d
                    k = j
            res[i] = k
            old = vals.get(val)
            vals[val] = (depth, i)
            for j in t[i]:
                if j == prev:
                    continue
                visit(j, i, depth + 1, vals)
            if old is not None:
                vals[val] = old
            else:
                vals.pop(val)
            
        visit(0, -1, 0, vals)
        return res