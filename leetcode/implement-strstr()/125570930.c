// title: implement-strstr()
// detail: https://leetcode.com/submissions/detail/125570930/
// datetime: Fri Oct 27 18:42:13 2017
// runtime: 3 ms
// memory: N/A

int strStr(char* haystack, char* needle) {
    
    int haystack_len = strlen(haystack);
    int needle_len = strlen(needle);
    int i, j;
    // 特殊情况
    if(needle_len == 0){
        return 0;
    }
    if(haystack_len == 0 && needle_len > 0){
        return -1;
    }
    
    for(i = 0; i < haystack_len; i ++){
        for(j = 0; j < needle_len; j ++){
            if(i + j < haystack_len){
                if(haystack[i + j] != needle[j]){
                    break;
                }
            } else {
                return -1;
            } 
        }
        if(j == needle_len){
            return i;
        }
    }
    return -1;
    
}