# title: lexicographical-numbers
# detail: https://leetcode.com/submissions/detail/285254021/
# datetime: Wed Dec 11 21:17:23 2019
# runtime: 100 ms
# memory: 18.1 MB

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(map(str, range(1, n + 1)))
            