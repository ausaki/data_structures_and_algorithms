// title: longest-common-prefix
// detail: https://leetcode.com/submissions/detail/116081652/
// datetime: Tue Aug 29 17:38:10 2017
// runtime: 3 ms
// memory: N/A

char* longestCommonPrefix(char** strs, int strsSize) {
    int length = 50;
    char* result = (char*)malloc(length);
    int i = 0,
        j = 0,
        k = 0;
    char c = 0;
    char match = 0;
    if(strsSize == 0){
        result = "";
        return result;
    }
    while(1){
        c = ((char*)strs[0])[i];
        if(c == 0){
            break;
        }
        match = 1;
        for(j = 1; j < strsSize; j ++){
            if(((char*)strs[j])[i] == 0){
                match = 0;
                break;
            }
            if(((char*)strs[j])[i] != c){
                match = 0;
                break;
            }
        }
        if(match){
            if(k >= length){
                length += 10;
                result = (char*)realloc(result, length);
            }
            result[k++] = c;
        } else {
            break;
        }
        i ++;
    }
    result[k] = 0;
    return result;
}