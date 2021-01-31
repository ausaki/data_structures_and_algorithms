def find_longest_palindrome(sequence):
    N = len(sequence)
    longest = 1
    c = 0
    l = 0
    for i in range(N):
        j = 0
        # odd
        while (i - j >= 0) and (i + j < N) and sequence[i - j] == sequence[i + j]:
            j += 1
        l = 2 * j - 1
        if l > longest:
            longest = l
            c = i
        # even
        j = 0
        while (i - j >= 0) and (i + 1 + j < N) and sequence[i - j] == sequence[i + 1 + j]:
            j += 1
        l = 2 * j - 2
        if l > longest:
            longest = l
            c = i
    return sequence[c - (longest - 1) // 2: c + longest // 2 + 1]
            

def manacher(sequence):
    n = len(sequence)
    d1, d2 = [0] * n, [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 1 if i > r else (1 + min(d1[l + r - i], r - i))
        while i - k >= 0 and i + k < n and sequence[i - k] == sequence[i + k]:
            k += 1
        k -= 1
        d1[i] = k
        if i + k > r:
            l, r = i - k, i + k
    l, r = 0, -1
    for i in range(n):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while i - k - 1 >= 0 and i + k < n and sequence[i - k - 1] == sequence[i + k]:
            k += 1
        d2[i] = k
        if i + k > r:
            l, r = i - k - 1, i + k
    l, r = -1, -1
    for i in range(n):
        l1, r1 = i - d1[i], i + d1[i]
        if r1 - l1 > r - l:
            l, r = l1, r1
        l1, r1 = i - d2[i], i + d2[i] - 1
        if r1 - l1 > r - l:
            l, r = l1, r1
    return sequence[l: r + 1]

if __name__ == '__main__':
    sequence = 'abcdefgfedc'
    print(sequence)
    # print(find_longest_palindrome(sequence))
    print(manacher(sequence))