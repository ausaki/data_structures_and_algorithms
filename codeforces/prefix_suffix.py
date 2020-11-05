'''
You have a string s = s1s2...s|s|, where |s| is the length of string s, and si its i-th character.

Let's introduce several definitions:

    A substring s[i..j] (1 ≤ i ≤ j ≤ |s|) of string s is string sisi + 1...sj.
    The prefix of string s of length l (1 ≤ l ≤ |s|) is string s[1..l].
    The suffix of string s of length l (1 ≤ l ≤ |s|) is string s[|s| - l + 1..|s|]. 

Your task is, for any prefix of string s which matches a suffix of string s, print the number of times it occurs in string s as a substring.
'''

def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[j] != s[i]:
            j = pi[j - 1]
        pi[i] = j + (s[j] == s[i])
    return pi

def solve(s):
    n = len(s)
    pi = prefix_function(s)
    j = n
    prefixes = []
    while j:
        prefixes.append(j)
        j = pi[j - 1]
    print(len(prefixes))
    if len(prefixes) == 1:
        print(n, 1)
        return
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[pi[i]] += 1
    for i in range(n - 1, 0, -1):
        cnt[pi[i - 1]] += cnt[i]
    for i in range(n + 1):
        cnt[i] += 1
    for i in reversed(prefixes):
        print(i, cnt[i])

def main():
    s = input()
    solve(s)

main()
    


