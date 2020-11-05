'''
https://cp-algorithms.com/string/suffix-array.html
https://en.wikipedia.org/wiki/Suffix_array
'''
def suffix_array_count_sort(s):
    s += '$'
    b = ord('$')
    K = ord(max(s)) - b + 1
    
    n = len(s)
    p = [0] * n
    c = [0] * n
    cnt = [0] * max(K, n)
    for i in range(n):
        cnt[ord(s[i]) - b] += 1
    for i in range(1, K):
        cnt[i] += cnt[i - 1]
    for i in range(n - 1, -1, -1):
        j = ord(s[i]) - b
        cnt[j] -= 1
        p[cnt[j]] = i
    c[p[0]] = 0
    rank = 1
    for i in range(1, n):
        if s[p[i - 1]] != s[p[i]]:
            rank += 1
        c[p[i]] = rank - 1
    h = 0
    pn = [0] * n
    cn = [0] * n
    while (1 << h) < n:
        pn[:] = ((p[i] - (1 << h) + n) % n for i in range(n))
        cnt[:rank] = (0 for i in range(rank))
        for i in range(n):
            cnt[c[pn[i]]] += 1
        for i in range(1, rank):
            cnt[i] += cnt[i - 1]
        for i in range(n - 1, -1, -1):
            j = c[pn[i]]
            cnt[j] -= 1
            p[cnt[j]] = pn[i]
        rank = 1
        for i in range(1, n):
            curr = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i - 1]], c[(p[i - 1] + (1 << h)) % n])
            if curr != prev:
                rank += 1
            cn[p[i]] = rank - 1
        c, cn = cn, c
        h += 1
    p.pop(0)
    return p

def main():
    s = input()
    arr = suffix_array_count_sort(s)
    print('\n'.join(map(str, arr)))

main()


