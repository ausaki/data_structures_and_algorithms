# title: count-items-matching-a-rule
# detail: https://leetcode.com/submissions/detail/461506462/
# datetime: Sun Feb 28 10:33:50 2021
# runtime: 240 ms
# memory: 20.6 MB

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        i = 0
        if ruleKey == 'type':
            i = 0
        elif ruleKey == 'color':
            i = 1
        else:
            i = 2
        for item in items:
            if item[i] == ruleValue:
                res += 1
        return res