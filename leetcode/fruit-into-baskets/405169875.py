# title: fruit-into-baskets
# detail: https://leetcode.com/submissions/detail/405169875/
# datetime: Tue Oct  6 15:03:03 2020
# runtime: 720 ms
# memory: 19.9 MB

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        s = {tree[0]}
        i = 0
        j = 0
        total = 0
        result = 0
        for k, t in enumerate(tree):
            if t != tree[j]:
                i, j = j, k
            s.add(t)
            if len(s) == 3:
                total = j - i
                s = {tree[i], t}
            total += 1
            result = max(result, total)
        return result
        