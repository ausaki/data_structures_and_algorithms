# title: goal-parser-interpretation
# detail: https://leetcode.com/submissions/detail/429211303/
# datetime: Thu Dec 10 20:24:24 2020
# runtime: 32 ms
# memory: 14.4 MB

class Solution:
    def interpret(self, command: str) -> str:
        s = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                i += 1
                s.append('G')
            elif command[i + 1] == ')':
                i += 2
                s.append('o')
            else:
                i += 4
                s.append('al')
        return ''.join(s)