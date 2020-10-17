# title: prime-palindrome
# detail: https://leetcode.com/submissions/detail/406918762/
# datetime: Sat Oct 10 21:22:05 2020
# runtime: 160 ms
# memory: 14 MB

class Solution:
    def primePalindrome(self, N: int) -> int:
        def make_palindrome(n):
            if n == 1:
                for i in range(10):
                    yield i
                return
            h = n // 2
            # if n % 2
            for i in range(10 ** (h - 1), 10 ** h):
                j = i
                r = 0
                while j:
                    j, k = divmod(j, 10)
                    r = r * 10 + k
                if n % 2:
                    for j in range(10):
                        yield i * (10 ** (h + 1)) + j * (10 ** h) + r
                else:
                    yield i * (10 ** h) + r
                    
        def isprime(x):
            if x == 1:
                return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True
        
        n = len(str(N))
        for i in range(n, 10):
            for num in make_palindrome(i):
                if num >= N and isprime(num):
                    return num
        