# title: filling-bookcase-shelves
# detail: https://leetcode.com/submissions/detail/397404035/
# datetime: Fri Sep 18 16:46:45 2020
# runtime: 56 ms
# memory: 15.4 MB

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            w = 0
            h = 0
            result = 10 ** 8
            for j in range(i, n):
                w += books[j][0]
                h = max(h, books[j][1])
                if w <= shelf_width:
                    result = min(result, h + dp(j + 1))
                else:
                    break
            return result
        
        result = dp(0)
        return result