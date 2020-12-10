# title: minimum-moves-to-make-array-complementary
# detail: https://leetcode.com/submissions/detail/425289351/
# datetime: Sun Nov 29 15:34:23 2020
# runtime: 1268 ms
# memory: 28.9 MB

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        '''
        sweep line
        
        
        '''
        events = [0] * (2 * limit + 2)
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            events[min(a, b) + 1] -= 1
            events[a + b] -= 1
            events[a + b + 1] += 1
            events[max(a, b) + limit + 1] += 1
            
        curr = n
        ans = math.inf
        for ev in range(2, 2 * limit + 1):
            curr += events[ev]
            ans = min(ans, curr)
        return ans   