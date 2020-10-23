# title: chalkboard-xor-game
# detail: https://leetcode.com/submissions/detail/411076369/
# datetime: Tue Oct 20 22:53:11 2020
# runtime: 68 ms
# memory: 14.2 MB

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        def play(cnt, xor):
            for k in cnt:
                if k != xor and cnt[k] > 0:
                    cnt[k] -= 1
                    if not play(cnt, xor ^ k):
                        cnt[k] += 1
                        return True
                    cnt[k] += 1
            return False
        cnt = collections.Counter(nums)
        xor = 0
        x = 0
        for k, v in cnt.items():
            if v % 2:
                xor ^= k
                x += 1
        if xor == 0 or x % 2 == 0:
            return True
        return False
