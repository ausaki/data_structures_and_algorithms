// title: remove-k-digits
// detail: https://leetcode.com/submissions/detail/281537669/
// datetime: Mon Nov 25 16:24:40 2019
// runtime: 16 ms
// memory: 7.2 MB

char * removeKdigits(char * num, int k){
    int N = strlen(num);
    int i = 0, j;
    while(i < N - 1 && k > 0){
        if(num[i] <= num[i + 1]){
            i ++;
            continue;
        }
        // for(j = i + 1; j < N; j++){
        //     num[j - 1] = num[j];
        // }
        memmove(num + i, num + i + 1, N - i - 1);
        k -= 1;
        N--;
        i--;
        if(i < 0) i = 0;
    }
    if(k > 0){
        N -= k;
        if(N < 0) N = 0;
    }
    num[N] = 0;
    while(num[0] == '0'){
        num++;
        N--;
    }
    if(N == 0){
        return "0";
    }
    num[N] = 0;
    return num;
}

