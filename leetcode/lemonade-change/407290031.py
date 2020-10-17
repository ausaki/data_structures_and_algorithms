# title: lemonade-change
# detail: https://leetcode.com/submissions/detail/407290031/
# datetime: Sun Oct 11 16:33:25 2020
# runtime: 128 ms
# memory: 14.3 MB

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = {5: 0, 10: 0}
        for b in bills:
            if b == 5:
                cnt[b] += 1
            elif b == 10:
                if cnt[5] > 0:
                    cnt[5] -= 1
                    cnt[10] += 1
                else:
                    return False
            else:
                if cnt[10] > 0:
                    if cnt[5] > 0:
                        cnt[5] -= 1
                        cnt[10] -= 1
                    else:
                        return False
                else:
                    if cnt[5] > 2:
                        cnt[5] -= 3
                    else:
                        return False
        return True