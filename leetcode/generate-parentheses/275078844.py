# title: generate-parentheses
# detail: https://leetcode.com/submissions/detail/275078844/
# datetime: Fri Nov  1 22:05:02 2019
# runtime: 44 ms
# memory: 14.1 MB

class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self._gen(n, n, '', results)
        return results
    
    def _gen(self, left_parens, right_parens, s, results):
        if left_parens == 0 and right_parens == 0:
            results.append(s)
            return
        
        if left_parens:
            self._gen(left_parens - 1, right_parens, s + '(', results)
        
        if right_parens and left_parens < right_parens:
            self._gen(left_parens, right_parens - 1, s + ')', results)
        
            
        