// title: zigzag-conversion
// detail: https://leetcode.com/submissions/detail/283652576/
// datetime: Wed Dec  4 17:19:57 2019
// runtime: 4 ms
// memory: 8 MB



char * convert(char * s, int numRows){
    int N = strlen(s);
    int T = 2 * numRows - 2;
    if(T <= 0){
        return s;
    }
    char *res = (char *)malloc(N + 1);
    res[N] = 0;
    int i, j, m, k = 0;
    for(i = 0; i < numRows; i++){
        j = i;
        while(j < N){
            res[k] = s[j];
            k += 1;
            m = j % T;
            if(m < numRows - 1){
                j += (T - 2 * m);
            } else if(m == numRows - 1) {
                j += T;
            } else{
                j += 2 * (T - m);
            }
        }
    }
    return res;
}

