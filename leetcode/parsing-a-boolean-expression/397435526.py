# title: parsing-a-boolean-expression
# detail: https://leetcode.com/submissions/detail/397435526/
# datetime: Fri Sep 18 19:09:14 2020
# runtime: 52 ms
# memory: 14 MB

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        exp = expression
        op = {'!': operator.not_, '&': operator.and_, '|': operator.or_}
        def parse(i):
            if exp[i] == 't':
                return True, i + 1
            if exp[i] == 'f':
                return False, i + 1
            if exp[i] in op:
                e = exp[i]
                o = op[exp[i]]
                val = None
                i += 2
                while True:
                    v, i = parse(i)
                    if val is None:
                        val = v
                    else:
                        val = o(val, v)
                    i += 1
                    if exp[i - 1] == ')':
                        break
                if e == '!':
                    val = o(val)
                return val, i
        v, i = parse(0)
        return v
            