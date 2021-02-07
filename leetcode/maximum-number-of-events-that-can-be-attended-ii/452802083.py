# title: maximum-number-of-events-that-can-be-attended-ii
# detail: https://leetcode.com/submissions/detail/452802083/
# datetime: Sun Feb  7 00:49:29 2021
# runtime: 1252 ms
# memory: 59.3 MB

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n=len(events)
        cur=[0]*n
        lookup=[-1]*n
        for _ in range(k):
            nxt=[0]*n
            for j in range(n):
                if j==0:
                    nxt[j]=events[j][2]
                elif events[0][1]>=events[j][0]:
                    nxt[j]=max(nxt[j-1],events[j][2])
                else:
                    if lookup[j]==-1:
                        lo,hi=0,j-1
                        while lo<hi:
                            mid=(lo+hi+1)//2
                            if events[mid][1]>=events[j][0]:
                                hi=mid-1
                            else:
                                lo=mid
                        lookup[j]=lo
                    nxt[j]=max(nxt[j-1],events[j][2]+cur[lookup[j]])
            cur=nxt
        return cur[-1]

