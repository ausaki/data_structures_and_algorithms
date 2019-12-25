// title: decode-ways
// detail: https://leetcode.com/submissions/detail/146552084/
// datetime: Fri Mar 23 16:41:34 2018
// runtime: 48 ms
// memory: N/A

int numDecodings_(char* s, int start, int* cache){
    if(s[start] == 0){
        return 1;
    }
    if(cache[start] >= 0){
        return cache[start];
    }
    int a = s[start];
    int b = s[start + 1];
    int c = 0;
    if(a >= '1' && b <= '9'){
        c += numDecodings_(s, start + 1, cache);
    }
    if((a == '1' && b >= '0' && b <= '9') || 
       (a == '2' && b >= '0' && b <= '6')){
        c += numDecodings_(s, start + 2, cache);
    }
    cache[start] = c;
    return c;
}
int numDecodings(char* s) {
    if(s[0] == 0){
        return 0;
    }
    int l = strlen(s);
    int* cache = (int*)malloc(l * sizeof(int));
    int i = 0;
    for(i = 0; i < l; i ++){
        cache[i] = -1;
    }
    return numDecodings_(s, 0, cache);
}