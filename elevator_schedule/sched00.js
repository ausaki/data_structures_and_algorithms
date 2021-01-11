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

        let setElevatorDirection = function(elevator, dir){
            if(dir == 1){
                elevator.goingUpIndicator(true);
                elevator.goingDownIndicator(false);
            }else if (dir == -1){
                elevator.goingUpIndicator(false);
                elevator.goingDownIndicator(true);
            } else {
                elevator.goingUpIndicator(false);
                elevator.goingDownIndicator(false);
            }
        }
        
        let getElevatorDirection = function(elevator){
            let up = elevator.goingUpIndicator();
            let down = elevator.goingDownIndicator();
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

        let reverseElevatorDirection = function(elevator){
            let d = getElevatorDirection(elevator);
            if(d == 0 || d == -2){
                return;
            }
            setElevatorDirection(elevator, -d);
        }

        let setElevatorDirectionAuto = function(elevator){
            let d = getElevatorDirection(elevator);
            let curr = elevator.currentFloor();
            if(curr == floors.length - 1){
                setElevatorDirection(elevator, -1);
                return;
            }
            if(curr == 0){
                setElevatorDirection(elevator, 1);
                return;
            }
            let q = elevator.destinationQueue;
            if(q.length > 0){
                if(q[0] > curr){
                    d = 1;
                } else if(q[0] < curr){
                    d = -1;
                }
            } else {
                if(upcmds[curr] == 1){
                    d = 1;
                } else if(downcmds[curr] == 1){
                    d = -1;
                }
            }
            setElevatorDirection(elevator, d);
        }
        let schedule = function(elevator, event, passing_floor=-1){
            /*
             * 调度算法: 上下扫描法 
             */
            let q = elevator.destinationQueue;
            let dir = getElevatorDirection(elevator);
            let curr_floor = elevator.currentFloor();
            let floors = elevator.getPressedFloors();
            let f = -1;

            if(q.length > 0 && event == EV_PASSING_FLOOR){
                /* 
                 * 当前事件是 EV_PASSING_FLOOR, 此时必须检查是否停在即将抵达的楼层, 条件如下:
                 * 乘客的目的楼层是该楼层, 或者该楼层有人等待电梯.
                 */
                if(dir == 1){
                    if(floors.indexOf(passing_floor) >= 0 || (upcmds[passing_floor] == 1)){
                        elevator.goToFloor(passing_floor, true);
                    }
                } else if(dir == -1){
                    if(floors.indexOf(passing_floor) >= 0 || downcmds[passing_floor] == 1){
                        elevator.goToFloor(passing_floor, true);
                    }
                }
                console.log("schedule", event, JSON.stringify(elevator.destinationQueue));
                return;
            }
            // 到顶楼了, 切换方向
            if(curr_floor == NFLOORS - 1){
                elevator.goToFloor(0);
            }
            if(curr_floor == 0){
                elevator.goToFloor(NFLOORS - 1);
            }
            console.log("schedule", event, JSON.stringify(elevator.destinationQueue));
            setElevatorDirectionAuto(elevator);
        };

        let schedule_elevators = function(){
            for(let i = 0; i < NELEVATORS; i++){
                schedule(elevators[i], EV_UP_BUTTON_PRESSED);
            }
        };

        /* 初始化事件处理器 */

        let upcmds = [];
        let downcmds = [];

        for(let i = 0; i < NELEVATORS; i++){
            setElevatorDirection(elevators[i], 0);
            elevators[i].on(EV_IDLE, function() {
                console.log("idle");
            });
            elevators[i].on(EV_STOPPED_AT_FLOOR, function(floor_num) {
                console.log("STOP", floor_num);
                schedule(elevators[i], EV_STOPPED_AT_FLOOR);
                let d = getElevatorDirection(elevators[i]);
                if(d == 1){
                    upcmds[floor_num] = 0;
                } else {
                    downcmds[floor_num] = 0;
                }
            });
            
            elevators[i].on(EV_FLOOR_BUTTON_PRESSED, function(floor_num) {
                console.log("GO", floor_num);
                schedule(elevators[i], EV_FLOOR_BUTTON_PRESSED);
            });
            
            elevators[i].on(EV_PASSING_FLOOR, function(floor_num, direction) {
                console.log("PASSING", floor_num, direction);
                schedule(elevators[i], EV_PASSING_FLOOR, floor_num);
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
                schedule_elevators();
            });
            floors[i].on(EV_DOWN_BUTTON_PRESSED, function(){
                console.log("DOWN", i);
                // 设置 downcmds[i], 表示有人在 i 楼按了向下按钮
                downcmds[i] = 1;
                schedule_elevators();
            });
        }
    },
    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}

