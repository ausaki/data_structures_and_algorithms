# title: most-common-word
# detail: https://leetcode.com/submissions/detail/409301407/
# datetime: Fri Oct 16 11:45:35 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        return collections.Counter(filter(lambda w: w not in banned, map(lambda m: m.group(1).lower(), re.finditer(r'\b(\w+)\b', paragraph)))).most_common(1)[0][0]