// title: longest-substring-without-repeating-characters
// detail: https://leetcode.com/submissions/detail/76078941/
// datetime: Tue Sep 27 21:06:36 2016
// runtime: 49 ms
// memory: N/A

int lengthOfLongestSubstring(char* s) {
    int maxLength = 0;
    int length = 0;
    char *s0 ,*s1;
    char ch = 0;
    int i;
    unsigned char dict[128] = {0};
    for(i = 0; i < 128; i++){
            dict[i] = 0;
    }
    s0 = s;
    while(*s0 != 0){
        for(i = 0; i < 128; i++){
            dict[i] = 0;
        }
        s1 = s0;
        ch = 0;
        length = 0;
        while(*s1 != 0){
            if(dict[*s1] == 1){
                ch = *s1;
                while(*(--s1) != ch){
                }
                break;
            } else {
                dict[*s1] = 1;
                length ++;
            }
            s1 ++;
        }
        if(length > maxLength){
            maxLength = length;
        }
        if(ch != 0){
            s0 = s1 + 1;
        } else{
            s0 ++;
        }
    }
    return maxLength;
}