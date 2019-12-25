// title: longest-substring-without-repeating-characters
// detail: https://leetcode.com/submissions/detail/76078378/
// datetime: Tue Sep 27 20:56:45 2016
// runtime: 52 ms
// memory: N/A

int lengthOfLongestSubstring(char* s) {
    int maxLength = 0;
    int length = 0;
    char *s0 ,*s1;
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
        length = 0;
        while(*s1 != 0){
            if(dict[*s1] == 1){
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
        s0 ++;
    }
    return maxLength;
}