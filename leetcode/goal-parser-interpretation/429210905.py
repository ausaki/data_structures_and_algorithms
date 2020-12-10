# title: goal-parser-interpretation
# detail: https://leetcode.com/submissions/detail/429210905/
# datetime: Thu Dec 10 20:22:04 2020
# runtime: 28 ms
# memory: 14.3 MB

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')