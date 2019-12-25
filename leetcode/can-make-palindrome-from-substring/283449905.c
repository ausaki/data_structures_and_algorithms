// title: can-make-palindrome-from-substring
// detail: https://leetcode.com/submissions/detail/283449905/
// datetime: Tue Dec  3 22:33:24 2019
// runtime: 316 ms
// memory: 44.2 MB



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* canMakePaliQueries(char * s, int** queries, int queriesSize, int* queriesColSize, int* returnSize){
    int N = strlen(s);
    int cache[N];
    bool *answer = (bool *)malloc(sizeof(bool) * queriesSize);
    int i, j, k, l, r;
    cache[0] = 1 << (s[0] - 'a');
    for(i = 1; i < N; i++){
        cache[i] = (1 << (s[i] - 'a')) ^ cache[i - 1];
    }
    for(i = 0; i < queriesSize; i++){
        l = queries[i][0];
        r = queries[i][1];
        j = cache[r] ^ (l > 0 ? cache[l - 1] : 0);
        k = 0;
        while(j){
            k += 1;
            j &= j - 1;
        }
        answer[i] = (k / 2) <= queries[i][2];
    }
    *returnSize = queriesSize;
    return answer;
}

