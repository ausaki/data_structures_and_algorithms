{
    init: function(elevators, floors) {
        let NFLOORS = floors.length,
            NELEVATORS = elevators.length;
        let EV_IDLE = "idle",
            EV_FLOOR_BUTTON_PRESSED = "floor_button_pressed",
            EV_PASSING_FLOOR = "passing_floor",
            EV_STOPPED_AT_FLOOR = "stopped_at_floor",
            EV_UP_BUTTON_PRESSED = "up_button_pressed",
            EV_DOWN_BUTTON_PRESSED = "down_button_pressed";

        function setElevatorDirection (dir){
            /**
             * 设置电梯运行方向
             * dir = 1 表示上
             * dir = -1 表示下
             * dir = 0 表示停止
             * dir = 其它 表示非法
             */
            if(dir == 1){
                this.goingUpIndicator(true);
                this.goingDownIndicator(false);
            }else if (dir == -1){
                this.goingUpIndicator(false);
                this.goingDownIndicator(true);
            } else if(dir == 0) {
                this.goingUpIndicator(false);
                this.goingDownIndicator(false);
            }
        }
        
        function getElevatorDirection(){
            let up = this.goingUpIndicator();
            let down = this.goingDownIndicator();
            if(up && !down){
                return 1;
            }
            if(!up && down){
                return -1;
            }
            if(!up && !down){
                return 0;
            }
            return -2;
        }

        function reverseElevatorDirection (){
            let d = this.getElevatorDirection();
            if(d == 0 || d == -2){
                return;
            }
            this.setElevatorDirection(-d);
        }

        function setElevatorDirectionAuto (){
            /**
             * 自动根据当前状态设置电梯的运行方向
             */
            let d = this.getElevatorDirection();
            let curr = this.currentFloor();
            if(curr == floors.length - 1){
                // 到了顶层肯定要调转方向
                this.setElevatorDirection(-1);
                return;
            }
            if(curr == 0){
                // 到了第 1 层肯定要调转方向
                this.setElevatorDirection(1);
                return;
            }
            let q = this.destinationQueue;
            if(q.length > 0){
                // 如果队列不为空, 那么根据目的楼层设置运行方向. 注意: 按理来说 q[0] != curr, 但是这里还是保持下面的写法.
                if(q[0] > curr){
                    d = 1;
                } else if(q[0] < curr){
                    d = -1;
                }
            } else {
                // 如果队列空, 那么根据乘客请求设置运行方向.
                if(this.upcmds[curr] == 1){
                    d = 1;
                } else if(this.downcmds[curr] == 1){
                    d = -1;
                } else {
                    d = 0;
                }
            }
            this.setElevatorDirection(d);
        }

        function search_cmd(cmds, start, end, reverse=false){
            /* 从 cmds[start: end] 中搜索第一个合适的楼层 */
            if(!reverse){
                for(let i = start; i < end; i++){
                    if(cmds[i] == 1){
                        return i;
                    }
                }
                return NFLOORS;
            }
            for(let i = end - 1; i >= start; i--){
                if(cmds[i] == 1){
                    return i;
                }
            }
            return -1;
        }

        function seachDestFloor(){
            /**
             * 搜索最佳目的楼层
             */
            let dir = this.getElevatorDirection();
            let curr_floor = this.currentFloor();
            let floors = this.getPressedFloors();
            let f = -1;

            if(dir == 0){
                // let f1 = -1, f2 = -1;
                // this.setElevatorDirection(1)
                // f1 = this.seachDestFloor();
                // return f1
                for(let i = 0; i < NFLOORS; i++){
                    if(this.upcmds[i] == 1 || this.downcmds[i] == 1){
                        return i;
                    }
                }
                return 0;
            }
            if(dir == 1){
                f = -1;
                // 当前运行方向为向上
                // 找出最高的目的楼层.
                if(floors.length > 0){
                    f = Math.max(...floors);
                    if(f <= curr_floor){
                        f = -1;
                    }
                }
                f = Math.max(f, search_cmd(this.upcmds, curr_floor + 1, NFLOORS, true));
                if(!(f >= 0 && f < NFLOORS)){
                    f = search_cmd(this.downcmds, curr_floor + 1, NFLOORS, true);
                }
                // 找出最低的楼层
                if(!(f >= 0 && f < NFLOORS)){
                    if(floors.length > 0){
                        f = Math.min(...floors);
                    }
                    let f1 = search_cmd(this.downcmds, 0, curr_floor);
                    if(!(f >= 0 && f < NFLOORS) || f1 < f){
                        f = f1;
                    }
                }
                if(!(f >= 0 && f < NFLOORS)){
                    f = search_cmd(this.upcmds, 0, curr_floor);
                }
                return f
            }
            // f == -1, 当前运行方向为向下
            // 找出最低的楼层.
            f = NFLOORS;
            if(floors.length > 0){
                f = Math.min(...floors);
                if(f >= curr_floor){
                    f = NFLOORS;
                }
            }
            f = Math.min(f, search_cmd(this.downcmds, 0, curr_floor));
            if(!(f >= 0 && f < NFLOORS)){
                f = search_cmd(this.upcmds, 0, curr_floor)
            }
            // 找出最高的楼层
            if(!(f >= 0 && f < NFLOORS)){
                if(floors.length > 0){
                    f = Math.max(...floors);
                }
                let f1 = search_cmd(this.upcmds, curr_floor + 1, NFLOORS, true);
                if(!(f >= 0 && f < NFLOORS) || f1 > f){
                    f = f1;
                }
            }
            if(!(f >= 0 && f < NFLOORS)){
                f = search_cmd(this.downcmds, curr_floor + 1, NFLOORS, true);
            }
            return f
        }

        function schedule(event, passing_floor=-1){
            /**
             * 调度算法: 上下扫描法 
             * 
             * event: 事件类型
             * passing_floor: 如果事件 event = EV_PASSING_FLOOR 才有效, 表示电梯正要抵达的楼层.
             */

            let q = this.destinationQueue;
            let dir = this.getElevatorDirection();
            let curr_floor = this.currentFloor();
            let floors = this.getPressedFloors();
            let f = -1;

            if(event == EV_PASSING_FLOOR){
                /* 
                 * 当前事件是 EV_PASSING_FLOOR, 此时必须检查是否停在即将抵达的楼层, 条件如下:
                 * 乘客的目的楼层是该楼层, 或者该楼层有人等待电梯.
                 */
                if(floors.indexOf(passing_floor) >= 0){
                    this.goToFloor(passing_floor, true);
                    return;
                }
                if((dir == 1 && upcmds[passing_floor] == 1) || (dir == -1 && downcmds[passing_floor] == 1)){
                    this.goToFloor(passing_floor, true);
                }
                console.log("schedule", event, JSON.stringify(this.destinationQueue));
                return;
            }
            // 队列不为空, 那么直接返回
            if(q.length > 0){
                return;
            }
            f = this.seachDestFloor();
            if(f >= 0 && f < NFLOORS && q.indexOf(f) == -1){
                this.goToFloor(f, true);
            }
            console.log("schedule", event, JSON.stringify(this.destinationQueue));
            this.setElevatorDirectionAuto();
        };

        function distance(elevator, floor, direction){
            /**
             * 计算电梯到 floor 的距离
             */
            let dir = elevator.getElevatorDirection();
            let curr = elevator.currentFloor();
            let q = elevator.destinationQueue;
            let dst = q.length > 0 ? q[q.length - 1] : -1;
            if(dst == -1 || dir == 0){
                return Math.abs(curr - floor);
            }
            if(dir == direction && ((dir == 1 && floor > curr) || (dir == -1 && floor < curr))){
                return Math.abs(floor - curr);
            }
            return Math.abs(dst - curr) + Math.abs(dst - floor);
        }

        function schedule_elevators(floor, direction){
            /* 调度多部电梯 */
            let min_distance = 2 * NFLOORS;
            let min_i;
            for(let i = 0; i < NELEVATORS; i++){
                let d = distance(elevators[i], floor, direction);
                if(d < min_distance){
                    min_distance = d;
                    min_i = i;
                }
            }
            let elevator = elevators[min_i];
            if(direction == 1){
                elevator.upcmds[floor] = 1;
            } else {
                elevator.downcmds[floor] = 1;
            }
            console.log("schedule_elevators", elevator.id);
            elevator.schedule(direction == 1 ? EV_UP_BUTTON_PRESSED : EV_DOWN_BUTTON_PRESSED);
        };

        /* 保存乘客按下的上下按钮 */
        let upcmds = [];
        let downcmds = [];

        /* 初始化事件处理器 */
        for(let i = 0; i < NELEVATORS; i++){
            let e = elevators[i];
            e.getElevatorDirection = getElevatorDirection;
            e.setElevatorDirection = setElevatorDirection;
            e.setElevatorDirectionAuto = setElevatorDirectionAuto;
            e.schedule = schedule;
            e.seachDestFloor = seachDestFloor;
            e.upcmds = new Array(NFLOORS);
            e.downcmds = new Array(NFLOORS);
            e.id = i;

            for(let i = 0; i < NFLOORS; i++){
                e.upcmds[i] = e.downcmds[i] = 0;
            }

            e.setElevatorDirectionAuto();
            console.log(i, e.getElevatorDirection());

            e.on(EV_IDLE, function() {
                console.log("idle");
                this.setElevatorDirection(0);
            });
            e.on(EV_STOPPED_AT_FLOOR, function(floor_num) {
                console.log("STOP", floor_num);
                this.schedule(EV_STOPPED_AT_FLOOR);
                let d = this.getElevatorDirection();
                if(d == 1){
                    upcmds[floor_num] = 0;
                    this.upcmds[floor_num] = 0;
                } else {
                    downcmds[floor_num] = 0;
                    this.downcmds[floor_num] = 0;
                }
            });
            
            e.on(EV_FLOOR_BUTTON_PRESSED, function(floor_num) {
                console.log("GO", floor_num);
                this.schedule(EV_FLOOR_BUTTON_PRESSED);
            });
            
            e.on(EV_PASSING_FLOOR, function(floor_num, direction) {
                console.log("PASSING", floor_num, direction);
                this.schedule(EV_PASSING_FLOOR, floor_num);
            });
        }
        for(let i = 0; i < NFLOORS; i++){
            // 初始化 upcmds, upcmds
            upcmds.push(0);
            downcmds.push(0);
            // 设置 up_button_pressed, down_button_pressed
            floors[i].on(EV_UP_BUTTON_PRESSED, function(){
                console.log("UP", i);
                // 设置 upcmds[i], 表示有人在 i 楼按了向上按钮
                upcmds[i] = 1;
                schedule_elevators(i, 1);
            });
            floors[i].on(EV_DOWN_BUTTON_PRESSED, function(){
                console.log("DOWN", i);
                // 设置 downcmds[i], 表示有人在 i 楼按了向下按钮
                downcmds[i] = 1;
                schedule_elevators(i, -1);
            });
        }
    },
    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}

