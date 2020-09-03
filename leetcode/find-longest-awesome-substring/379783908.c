// title: find-longest-awesome-substring
// detail: https://leetcode.com/submissions/detail/379783908/
// datetime: Wed Aug 12 16:12:53 2020
// runtime: 20 ms
// memory: 6.4 MB



int longestAwesome(char * s){
    int result = 0;
    int prefix_sum[1024];
    int curr = 0;
    int i = 0, j = 0, k;
    char ch;
    prefix_sum[0] = -1;
    for(i = 1; i < 1024; i++){
        prefix_sum[i] = 1 << 20;
    }
    for(i = 0; s[i] != 0; i++){
        curr ^= 1 << (s[i] - 48);
        for(j = 0; j < 10; j++){
            k = i - prefix_sum[curr ^ (1 << j)];
            if(k > result){
                result = k;
            }
        }
        k = i - prefix_sum[curr];
        if(k > result){
            result = k;
        }
        if(i < prefix_sum[curr]){
            prefix_sum[curr] = i;
        }
    }
    return result;
}
