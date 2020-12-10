# title: minimum-moves-to-make-array-complementary
# detail: https://leetcode.com/submissions/detail/425293784/
# datetime: Sun Nov 29 15:50:24 2020
# runtime: 1280 ms
# memory: 28.4 MB

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        '''
        sweep line
        
        假设 S 是最优的目标和, 即经过最少的调整后每对数的和等于 S. (nums[i] + nums[n - 1 - i]) == S for i in range(n // 2).
        
        每对数最多需要替换 2 次使得其和等于 S. 总的有以下几种情况:
        
        - S == a + b, 这种情况需要替换 0 次.
        
        - S <= min(a, b), 这种情况需要替换 2 次.
        
        - min(a, b) < S <= max(a, b) + limit, 这种情况需要替换 1 次.
        
        - S > max(a, b) + limit, 这种情况需要替换 2 次.
        
        对每对数生成不同的事件, 然后扫描.
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