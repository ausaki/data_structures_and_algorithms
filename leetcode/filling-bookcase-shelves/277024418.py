# title: filling-bookcase-shelves
# detail: https://leetcode.com/submissions/detail/277024418/
# datetime: Fri Nov  8 16:20:45 2019
# runtime: 52 ms
# memory: 14.2 MB

from functools import lru_cache

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N = len(books)
        
        @lru_cache(None)
        def _dfs(i, w, h):
            if i >= N:
                return h
            h1 = h + _dfs(i + 1, books[i][0], books[i][1])
            if w + books[i][0] <= shelf_width:
                h2 = _dfs(i + 1, w + books[i][0], max(h, books[i][1]))
                return min(h1, h2)
            return h1
            
        
        return _dfs(0, 0, 0)