'''
https://www.geeksforgeeks.org/tiling-with-dominoes/

 A_{n} = A_{n-2} + 2*(B_{n-1}) 
 B_{n} = A_{n-1} + B_{n-2} 
'''

def count(n):
    if n % 2:
        return 0
    if n == 0:
        return 1
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    for i in range(2, n + 1):
        a = a0 + 2 * b1
        b = a1 + b0
        a0, a1 = a1, a
        b0, b1 = b1, b
    return a1

while True:
	n = int(input())
	if n == -1:
		break
	print(count(n))

