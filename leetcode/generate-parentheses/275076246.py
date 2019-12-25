# title: generate-parentheses
# detail: https://leetcode.com/submissions/detail/275076246/
# datetime: Fri Nov  1 21:43:44 2019
# runtime: 44 ms
# memory: 14 MB

class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        s = ''
        result = []
        self._gen(n, n, s, stack, result)
        return result
    
    def _gen(self, left_parens, right_parens, s, stack, result):
        if left_parens == 0 and right_parens == 0:
            result.append(s)
            return
        
        if left_parens:
            s += '('
            stack.append('(')
            self._gen(left_parens - 1, right_parens, s, stack, result)
            stack.pop()
            s = s[:-1]
        
        if right_parens and len(stack) > 0:
            stack.pop()
            s += ')'
            self._gen(left_parens, right_parens - 1, s, stack, result)
            stack.append('(')
            s = s[:-1]
        
            
        