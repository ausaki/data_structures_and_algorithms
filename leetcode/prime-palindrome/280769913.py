# title: prime-palindrome
# detail: https://leetcode.com/submissions/detail/280769913/
# datetime: Fri Nov 22 12:17:44 2019
# runtime: 136 ms
# memory: 12.8 MB

class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        def is_palindrome(n):
            m = 0
            k = n
            while k:
                k, i = divmod(k, 10)
                m = m * 10 + i
            return m == n
        
        def next_palindrome(n):
            if n == 9:
                return 11
            digits = str(n)
            n = len(digits)
            k = n // 2
            r = n % 2
            high = digits[:k]
            low = digits[k + r:]
            if high[::-1] > low:
                digits = high + (digits[k] if r else '') + high[::-1]
            else:
                high = str(int(digits[:k + r]) + 1)
                digits = high + high[:k][::-1]
            return int(digits)
            
        while True:
            if is_palindrome(N) and is_prime(N):
                return N
            N = next_palindrome(N)
            
        