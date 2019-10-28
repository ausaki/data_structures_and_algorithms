def distance(S, T):
    N = len(S)
    M = len(T)
    dp = []
    for i in range(N + 1):
        row = [0 for j in range(M + 1)]
        if i == 0:
            row = [j for j in range(M + 1)]
        else:
            row = [i if j == 0 else 0 for j in range(M + 1)]
        dp.append(row)

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min([
                    dp[i - 1][j] + 1,   # delete S[i - 1]
                    dp[i][j - 1] + 1,   # insert T[j - 1]
                    dp[i - 1][j - 1],        # S[i - 1] == T[j - 1]   
                ])
            else:
                dp[i][j] = min([
                    dp[i - 1][j] + 1,   # delete S[i - 1]
                    dp[i][j - 1] + 1,   # insert T[j - 1]
                    dp[i - 1][j - 1] + 1,    # replace S[i - 1] with T[j - 1]
                ])
    return dp[N][M]


if __name__ == '__main__':
    S = 'abcd'
    T = 'afccd'
    print(distance(S, T))
