# title: reconstruct-original-digits-from-english
# detail: https://leetcode.com/submissions/detail/285696071/
# datetime: Fri Dec 13 21:46:25 2019
# runtime: 44 ms
# memory: 12.9 MB

from collections import Counter, defaultdict
class Solution:
    def originalDigits(self, s: str) -> str:
        numbers = {
            'zero': '0', 'one': '1', 'two': '2',
            'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }
        # mapping = defaultdict(set)
        # for num in numbers:
        #     for ch in num:
        #         mapping[ch].add(num)
        # uniq = {}
        # while True:
        #     new_uniq = {}
        #     for ch, nums in mapping.items():
        #         if len(nums) == 1 and ch not in uniq:
        #             new_uniq[ch] = nums.pop()
        #     if not new_uniq:
        #         break
        #     for ch, num in new_uniq.items():
        #         for c in num:
        #             if c != ch:
        #                 mapping[c].discard(num)
        #     uniq.update(new_uniq)
        uniq = {'z': 'zero', 'w': 'two', 'u': 'four', 'x': 'six', 'g': 'eight', 'r': 'three', 'o': 'one', 't': 'three', 'h': 'three', 'f': 'five', 's': 'seven', 'e': 'nine', 'n': 'nine', 'i': 'nine'}
        res = ''
        counter = Counter(s)
        for ch, num in uniq.items():
            cnt = counter[ch]
            if cnt > 0:
                for c in num:
                    if c != ch:
                        counter[c] -= cnt
                res += numbers[num] * cnt
        res = ''.join(sorted(res))
        return res