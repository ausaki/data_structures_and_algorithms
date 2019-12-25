// title: valid-palindrome
// detail: https://leetcode.com/submissions/detail/190879040/
// datetime: Wed Nov 21 16:37:59 2018
// runtime: 4 ms
// memory: N/A

bool isAlphanumeric(char c){
    return (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
}

char toLowercase(char c){
    if(c >= 'A' && c <= 'Z'){
        return c + 'a' - 'A';
    }
    return c;
}

bool isPalindrome(char* s) {
    int i = 0,
        j = strlen(s) - 1;
    
    if(j - i <= 0){
        return true;
    }
    
    while(i <= j){
        while(i <= j && !isAlphanumeric(s[i])){
            i++;
        }
        while(i <= j && !isAlphanumeric(s[j])){
            j--;
        }
        if(i <= j && toLowercase(s[i]) != toLowercase(s[j])){
            return false;
        }
        i++;
        j--;
    }
    return true;
}