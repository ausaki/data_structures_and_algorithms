'''
A(n) = A(n - 1) + A(n - 2) + 2 * B(n - 1) + C(n - 1)
B(n) = A(n - 1) + B(n - 1)
C(n) = A(n - 1) + C(n - 2)

A(0) = 1, A(1) = 1
B(0) = 0, B(1) = 1
C(0) = 0, C(1) = 1
'''

A = [1, 1]
B = [0, 1]
C = [0, 1]

def count(n):
    if n <= 1:
        return 1
    for i in range(len(A), n + 1):
        A.append(A[-1] + A[-2] + 2 * B[-1] + C[-1])
        B.append(A[-2] + B[-1])
        C.append(A[-2] + C[-2])
    return A[n]

def main():
    m = int(input())
    for i in range(m):
        n = int(input())
        print('{} {}'.format(i + 1, count(n)))

main()