// title: self-crossing
// detail: https://leetcode.com/submissions/detail/60117098/
// datetime: Wed Apr 27 10:28:30 2016
// runtime: 0 ms
// memory: N/A


int min(int x, int y){
    return (x < y ? x : y);
}

int max(int x, int y){
    return (x > y ? x : y);
}

bool isCrossing(int * p1, int * p2, int x1, int y1, int x2, int y2){
    if(x1 == x2 && p1[1] == p2[1]){
        // the line[(x1, y1), (x2, y2] is vertical and other line(p1, p2) is horizontal
        if (x1 >= min(p1[0], p2[0]) && x1 <= max(p1[0], p1[0]) &&
            p1[1] >= min(y1, y2) && p1[1] <= max(y1, y2)){
            return true;
        }
        return false;
    } else if (y1 == y2 && p1[0] == p2[0]) {
        // the line[(x1, y1), (x2, y2)] is horizontal ans the other line(p1, p2) is vertical
        if (y1 >= min(p1[1], p2[1]) && y1 <= max(p1[1], p2[1]) &&
            p1[0] >= min(x1, x2) && p1[0] <= max(x1, x2)) {
            return true;        
        }
        return false;
    } else {
        // the both lines is paraller
        return false;
    }
}


bool isSelfCrossing(int* x, int xSize) {
    int i, j, x0, y0, x1, y1;
    int points[1000][2]={{0, 0}};
    if(xSize <= 3){
        return false;
    }
    x0 = y0 = x1 = y1 = 0;
    for(i = 0; i < 3; i ++){
        switch(i % 4){
            case 0:
                // move to north
                y1 += x[i];
                break;
            case 1:
                // move to west
                x1 -= x[i];
                break;
            case 2:
                // move to south
                y1 -= x[i];
                break;
            case 3:
                // move to east
                x1 += x[i];
                break;
            default:
                break;
        }
        points[i + 1][0] = x1;
        points[i + 1][1] = y1;
    }
    x0 = x1;
    y0 = y1;
    for(i = 3; i < xSize; i ++) {
        switch(i % 4){
            case 0:
                // move to north
                // y0 = y1;
                y1 += x[i];
                break;
            case 1:
                // move to west
                // x0 = x1;
                x1 -= x[i];
                break;
            case 2:
                // move to south
                // y0 = y1;
                y1 -= x[i];
                break;
            case 3:
                // move to east
                // x0 = x1;
                x1 += x[i];
                break;
            default:
                break;
        }
        if (x1 == 0 && y1 == 0){
            return true;
        }
        if(i % 4 == 0 || i % 4 == 2){
            // vertical
            j = 1;
        } else {
            // horizal
            j = 0;
        }
        for(; j < i - 1; j += 2){
            if(isCrossing(points[j], points[j + 1], x0, y0, x1, y1)){
                return true;
            }
        }
        points[i + 1][0] = x0 = x1;
        points[i + 1][1] = y0 = y1;
        
    }
    return false;
}

