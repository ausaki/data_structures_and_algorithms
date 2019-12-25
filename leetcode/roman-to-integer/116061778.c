// title: roman-to-integer
// detail: https://leetcode.com/submissions/detail/116061778/
// datetime: Tue Aug 29 14:36:55 2017
// runtime: 75 ms
// memory: N/A

int romanToInt(char* s) {
    short numbers[] = {
        0,0,100,500,0,0,0,
        0,1,0,0,50,1000,0,
        0,0,0,0,0,0,
        0,5,0,10,0,0,
    };
    int result = 0;
    int length = strlen(s);
    int i = 0;
    int delta = 0;
    int num = 0;
    while(s[i] != 0){
        num = numbers[s[i] - 'A'];
        if(i + 1 < length && (num == 1 || num == 10 || num == 100)){
            delta = numbers[s[i + 1] - 'A'] - num;
            if(delta > 0){
                result += delta;
                i ++;       
            } else {
                result += num;
            }
            
        } else {
            result += num;
        }
        i ++;
    }
    return result;
}