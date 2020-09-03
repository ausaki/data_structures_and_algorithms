# title: paint-house-iii
# detail: https://leetcode.com/submissions/detail/381230449/
# datetime: Sat Aug 15 22:09:33 2020
# runtime: 440 ms
# memory: 19.8 MB

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        bn=10**9
        
        @functools.lru_cache(None)
        def f(i, prevc, nhoodsleft):
            if i>=m:
                return 0 if nhoodsleft==0 else bn
            if nhoodsleft<0:
                return bn
            if m-i<nhoodsleft:
                return bn
            if houses[i]!=0:
                return f(i+1,houses[i],nhoodsleft-(1 if houses[i]!=prevc else 0))
            else:
                mm = min([bn if prevc<=0 else f(i+1,prevc,nhoodsleft)+cost[i][prevc-1]]+
                         [f(i+1,newc,nhoodsleft-1)+cost[i][newc-1] for newc in range(1,n+1) if newc!=prevc])
                return mm
        
        ff = f(0,-1,target)
        return ff if ff<bn else -1