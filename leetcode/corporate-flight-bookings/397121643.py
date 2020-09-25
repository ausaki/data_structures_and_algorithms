# title: corporate-flight-bookings
# detail: https://leetcode.com/submissions/detail/397121643/
# datetime: Fri Sep 18 01:58:29 2020
# runtime: 1120 ms
# memory: 27.9 MB

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookings.sort()
        m = len(bookings)
        q = []
        s = 0
        j = 0
        result = []
        for i in range(1, n + 1):
            while j < m and bookings[j][0] == i:
                heapq.heappush(q, bookings[j][1:])
                s += bookings[j][2]
                j += 1
            while q and q[0][0] < i:
                s -= heapq.heappop(q)[1]
            result.append(s)
        return result
            