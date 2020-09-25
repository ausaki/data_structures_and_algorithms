# title: parsing-a-boolean-expression
# detail: https://leetcode.com/submissions/detail/397433555/
# datetime: Fri Sep 18 18:59:12 2020
# runtime: 52 ms
# memory: 14.2 MB

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        exp = expression
        op = {'!': lambda a: not a[0], '&': all, '|': any}
        def parse(i):
            if exp[i] == 't':
                return True, i + 1
            if exp[i] == 'f':
                return False, i + 1
            if exp[i] in op:
                o = op[exp[i]]
                vals = []
                i += 2
                while True:
                    v, i = parse(i)
                    vals.append(v)
                    if exp[i] == ')':
                        i += 1
                        break
                    if exp[i] == ',':
                        i += 1
                return o(vals), i
        v, i = parse(0)
        return v
            