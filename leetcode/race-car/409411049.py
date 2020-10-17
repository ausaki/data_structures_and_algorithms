# title: race-car
# detail: https://leetcode.com/submissions/detail/409411049/
# datetime: Fri Oct 16 17:54:32 2020
# runtime: 1236 ms
# memory: 17.6 MB

class Solution:
    def racecar(self, target: int) -> int:
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps: continue

            for k in range(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ: steps2 -= 1 #No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]
                    
        
            
            