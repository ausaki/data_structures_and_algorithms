# title: minimum-number-of-frogs-croaking
# detail: https://leetcode.com/submissions/detail/383598348/
# datetime: Thu Aug 20 14:44:18 2020
# runtime: 172 ms
# memory: 14.5 MB

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        result = 0
        curr = 0
        letters = {'c': '', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        counter = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        for c in croakOfFrogs:
            if c == 'c':
                curr += 1
                result = max(result, curr)
            else:
                prev = letters[c]
                if counter[prev] == 0:
                    return -1
                counter[prev] -= 1
                if c == 'k':
                    curr -= 1
            counter[c] += 1
        return result if curr == 0 else -1