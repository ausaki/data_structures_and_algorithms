# title: shopping-offers
# detail: https://leetcode.com/submissions/detail/287988906/
# datetime: Mon Dec 23 21:54:45 2019
# runtime: 56 ms
# memory: 12.8 MB

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(needs, i):
            if i == len(special):
                return sum(n * price[j] for j, n in enumerate(needs))
            new_needs = list(needs)
            f = True
            for j, n in enumerate(new_needs):
                new_needs[j] -= special[i][j]
                if new_needs[j] < 0:
                    f = False
                    break
            if f:
                return min(special[i][-1] + dfs(new_needs, i), dfs(needs, i + 1))
            return dfs(needs, i + 1)
        
        # special.sort(key=lambda item: item[-1], reversed=True)
        return dfs(needs, 0)
            
                
            
                