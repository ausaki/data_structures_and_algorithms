# title: corporate-flight-bookings
# detail: https://leetcode.com/submissions/detail/397123492/
# datetime: Fri Sep 18 02:03:44 2020
# runtime: 1100 ms
# memory: 27.7 MB

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookings.sort(key=lambda k: k[0])
        m = len(bookings)
        q = []
        s = 0
        j = 0
        result = []
        for i in range(1, n + 1):
            while q and q[0][0] < i:
                s -= heapq.heappop(q)[1]
            while j < m and bookings[j][0] == i:
                heapq.heappush(q, bookings[j][1:])
                s += bookings[j][2]
                j += 1
            result.append(s)
        return result
            