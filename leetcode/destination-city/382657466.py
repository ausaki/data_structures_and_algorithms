# title: destination-city
# detail: https://leetcode.com/submissions/detail/382657466/
# datetime: Tue Aug 18 18:58:05 2020
# runtime: 56 ms
# memory: 13.8 MB

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set(b for a, b in paths) - set(a for a, b in paths)).pop()
