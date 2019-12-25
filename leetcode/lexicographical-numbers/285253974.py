# title: lexicographical-numbers
# detail: https://leetcode.com/submissions/detail/285253974/
# datetime: Wed Dec 11 21:16:57 2019
# runtime: 112 ms
# memory: 20.1 MB

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return map(int, sorted(map(str, range(1, n + 1))))
            