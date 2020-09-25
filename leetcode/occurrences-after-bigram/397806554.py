# title: occurrences-after-bigram
# detail: https://leetcode.com/submissions/detail/397806554/
# datetime: Sat Sep 19 18:47:36 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        return re.findall(r'(?=\b{} {} (\w+)\b)'.format(first, second), text)