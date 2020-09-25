# title: corporate-flight-bookings
# detail: https://leetcode.com/submissions/detail/397292270/
# datetime: Fri Sep 18 11:18:43 2020
# runtime: 892 ms
# memory: 27.8 MB

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        m = len(bookings)
        result = [0] * n
        for i, j, k in bookings:
            result[i - 1] += k
            if j < n:
                result[j] -= k
        for i in range(1, n):
            result[i] += result[i - 1]
        return result
            