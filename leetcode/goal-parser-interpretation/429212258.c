// title: goal-parser-interpretation
// detail: https://leetcode.com/submissions/detail/429212258/
// datetime: Thu Dec 10 20:30:02 2020
// runtime: 0 ms
// memory: 5.8 MB



char * interpret(char * command){
    int i = 0, j = 0;
    while(command[i]){
        if(command[i] == 'G'){
            command[j++] = 'G';
            i++;
        } else if (command[i + 1] == ')'){
            command[j++] = 'o';
            i += 2;
        } else {
            command[j++] = 'a';
            command[j++] = 'l';
            i += 4;
        }
    }
    command[j] = 0;
    return command;
}