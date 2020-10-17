# title: lemonade-change
# detail: https://leetcode.com/submissions/detail/407290806/
# datetime: Sun Oct 11 16:36:27 2020
# runtime: 136 ms
# memory: 14.4 MB

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = {5: 0, 10: 0}
        for b in bills:
            if b == 5:
                cnt[b] += 1
            elif b == 10:
                if cnt[5] == 0: return False
                cnt[5] -= 1
                cnt[10] += 1
            else:
                if cnt[10] > 0 and cnt[5] > 0:
                    cnt[5] -= 1
                    cnt[10] -= 1
                elif cnt[5] > 2:
                    cnt[5] -= 3
                else:
                    return False
        return True