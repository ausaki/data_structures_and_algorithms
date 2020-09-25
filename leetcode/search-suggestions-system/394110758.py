# title: search-suggestions-system
# detail: https://leetcode.com/submissions/detail/394110758/
# datetime: Fri Sep 11 15:40:37 2020
# runtime: 80 ms
# memory: 16.5 MB

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()
        prefix = ''
        result = []
        i = 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            result.append([products[i + j] for j in range(3) if i + j < n and products[i + j].startswith(prefix)])
        return result