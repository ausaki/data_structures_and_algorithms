# title: tree-of-coprimes
# detail: https://leetcode.com/submissions/detail/458390352/
# datetime: Sat Feb 20 23:27:09 2021
# runtime: 3032 ms
# memory: 116.7 MB

class Solution:
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
                if math.gcd(val, v) == 1 and d > max_depth:
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