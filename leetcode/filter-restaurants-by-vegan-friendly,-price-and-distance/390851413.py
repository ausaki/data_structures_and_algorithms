# title: filter-restaurants-by-vegan-friendly,-price-and-distance
# detail: https://leetcode.com/submissions/detail/390851413/
# datetime: Fri Sep  4 15:56:28 2020
# runtime: 372 ms
# memory: 22.4 MB

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        result = []
        for i, r, v, p, d in restaurants:
            if veganFriendly and not v:
                continue
            if p <= maxPrice and d <= maxDistance:
                result.append([r, i])
        result.sort(reverse=True)
        return [i for _, i in result]