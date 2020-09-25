# title: parsing-a-boolean-expression
# detail: https://leetcode.com/submissions/detail/397438067/
# datetime: Fri Sep 18 19:21:14 2020
# runtime: 92 ms
# memory: 20.4 MB

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        return eval(expression.translate(str.maketrans({'t': '1', 'f': '0', '!': 'not', '|': 'or_', '&': 'and_'})), {'or_': lambda *a: any(a), 'and_': lambda *a: all(a)})
            