# title: max-difference-you-can-get-from-changing-an-integer
# detail: https://leetcode.com/submissions/detail/383110131/
# datetime: Wed Aug 19 15:27:29 2020
# runtime: 36 ms
# memory: 13.7 MB

class Solution:
    def maxDiff(self, num: int) -> int:
        if num < 10:
            return 8
        digits = str(num)
        max_digits = min_digits = digits
        for i in range(len(digits)):
            if digits[i] != '9':
                max_digits = digits.replace(digits[i], '9')
                break
        if digits[0] != '1':
            min_digits = digits.replace(digits[0], '1')
        else:
            for i in range(1, len(digits)):
                if digits[i] != digits[0] and digits[i] != '0':
                    min_digits = digits.replace(digits[i], '0')
                    break
        # print(max_digits, min_digits)
        return int(max_digits) - int(min_digits)            
        