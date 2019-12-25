// title: roman-to-integer
// detail: https://leetcode.com/submissions/detail/116065681/
// datetime: Tue Aug 29 15:04:12 2017
// runtime: 68 ms
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
    int i = 0,
        j = 1;
    int delta = 0;
    int num1 = 0,
        num2 = 0;
    
    if(length == 0){
        return -1;
    }
    if(length == 1){
        return numbers[s[i] - 'A'];
    }
    
    while(j < length){
        num1 = numbers[s[i] - 'A'];
        num2 = numbers[s[j] - 'A'];
        delta = num2 - num1;
        if((num1 == 1 || num1 == 10 || num1 == 100) && delta > 0){
            result += delta;
            i = j + 1;    
        } else if(num2 != 1 && num2 != 10 && num2 != 100){
            result += num1 + num2;
            i = j + 1;
        } else {
            result += num1;
            i = j;
        }
        j = i + 1;
    }
    if(i == length - 1){
        result += numbers[s[i] - 'A'];
    }
    return result;
}