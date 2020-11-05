def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[j] != s[i]:
            j = pi[j - 1]
        pi[i] = j + (s[j] == s[i])
    return pi