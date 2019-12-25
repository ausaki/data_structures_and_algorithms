// title: longest-palindromic-substring
// detail: https://leetcode.com/submissions/detail/80267539/
// datetime: Thu Oct 27 17:04:58 2016
// runtime: 259 ms
// memory: N/A

char* longestPalindrome(char* s) {
    int length = strlen(s);
    int maxLength = 0;
    int left = 0;
    int i, j;
    char* result;
    for(i = length; i >= 1; i--){
        for(j = 0; j < length - i + 1; j ++){
            if(isPalindrome(s, j, j + i - 1) == 1){
                maxLength = i;
                left = j;
                break;
            }
        }
        if(maxLength != 0){
            break;
        }
    }
    
    // if(maxLength != 0){
        result = (char*)malloc(maxLength + 1);
        memcpy(result, s + left, maxLength);
        result[maxLength] = 0;
        return result;
    // }
}

int isPalindrome(char*s, int start, int end){
    int length = end - start + 1;
    while(start <= end){
        if(s[start ++] != s[end --]){
            return 0;
        }
    }
    return 1;
}