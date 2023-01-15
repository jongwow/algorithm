const COLOR = {
    BLUE: 2,
    RED: 1,
    WHITE: 0,
    WALL: 4,
};
const MAX_COUNT = 1000;

class Pos {
    constructor(x, y, n){
        this.x = x;
        this.y = y;
        this.n = n;
    }
    IsOutOfWall(){
        if(this.x >= this.n || this.y >= this.n || this.x < 0 || this.y < 0) {
            return true
        };
        return false;
    }
}
/**
 * x,y
 */
const DIR = {
    1: {x: 0, y: 1},
    2: {x: 0, y: -1},
    3: {x: 1, y: 0},
    4: {x: -1, y: 0},
}

class Dir {
    constructor(dir){
        if(dir === 1){
            this.x = 0;
            this.y = 1;
        }
        else if(dir=== 2){
            this.x = 0;
            this.y = -1;
        }
        else if(dir === 3){
            this.x = -1;
            this.y = 0;
        }
        else if(dir === 4){
            this.x = 1;
            this.y = 0;
        } else {
            throw new Error('invalid direction')
        }
    }
    reverse(){
        this.x = -this.x;
        this.y = -this.y;
    }
}
class OldHorse{
    constructor(index, position, direction){
        this.index = index;
        this.pos = position;
        this.dir = direction;
        this.movable = true;
        this.nextHorse = undefined;
    }
    nextMove(firstMove = true){
        if(this.movable === false){
            return;
        }
        let nextPosition = new Pos(this.pos.x + this.dir.x, this.pos.y + this.dir.y, this.pos.n)
        if(nextPosition.IsOutOfWall()){
            firstMove === true && this._moveNextBlue();
        } else {
            const nextTile = map[nextPosition.x][nextPosition.y];
            if(nextTile === COLOR.BLUE){
                firstMove === true && this._moveNextBlue();
            }
            if(nextTile === COLOR.RED){
                this._moveNextRed(nextPosition);
            }
            if(nextTile === COLOR.WHITE){
                this._moveNextWhite(nextPosition);
            }
        }
    }
    Mount(bottom){
        this.movable = false;
        let belowHorse = bottom;
        while(belowHorse.nextHorse){
            belowHorse = belowHorse.nextHorse;
        }
        belowHorse.nextHorse = this;
    }
    _moveNextBlue(){
       this.dir.reverse();
       this.nextMove(false);
    }
    _moveNextRed(nextPosition){
        //TODO 순서만 바꾸면 nextWhite랑 묶을수있나
        let previousHorse = this.reverseHorses();
        while(previousHorse){
            previousHorse.pos = nextPosition;
            previousHorse = previousHorse.nextHorse;
        }
    }
    _moveNextWhite(nextPos){
        let currentHorse = this;
        while(currentHorse){
            currentHorse.pos = nextPos;
            currentHorse = currentHorse.nextHorse;
        }
    }
    reverseHorses(){
        // traverseHorse
        let previousHorse = undefined;
        let nextHorse = undefined;
        let currentHorse = this;
        while(currentHorse){
            currentHorse.movable = false;
            nextHorse = currentHorse.nextHorse;
            currentHorse.nextHorse = previousHorse;
            previousHorse = currentHorse;
            currentHorse = nextHorse;
        }
        previousHorse.movable = true;
        return previousHorse;
    }
    countHorses(){
        let count = 1;
        let nextHorse = this.nextHorse;
        while(nextHorse){
            count++;
            nextHorse = nextHorse.nextHorse;
        }
        return count;
    }
}
class Horse{
    constructor(x, y, dir){
        this._x = x;
        this._y = y;
        this._dir = dir;
    }
    getX(){
        return this._x - 1;
    }
    getY(){
        return this._y - 1;
    }
    getDir(){
        return this._dir;
    }
}
const map = [];
const occupied = [];
// const horseMap = []; // x,y에 존재하는 horse list
const horses = [];

function printMap(map){
    for(let i =0; i < map.length; i++){
        console.log(map[i]);
    } 
}

function processInput(lines){
    const [N, K] = lines[0].split(" ").map((item) => +item); // N K
    for(let i = 1; i <= N; i++){
        const mapData = lines[i].split(" ").map((item) => +item);
        map.push(mapData);
        occupied.push(new Array(N).fill(undefined).map(() => undefined));
    }
    for(let i = N+1; i < N+1+K; i++){
        const [x, y, dir]= lines[i].split(" ").map((item) => +item);
        // horses.push(new Horse(x, y, dir));
        horses.push(new OldHorse(i - N, new Pos(x-1, y-1, N), new Dir(dir)));
    }
    for(let i = 0; i < horses.length; i++){
        //TODO: 처음부터 올라타면?
        const x = horses[i].pos.x;
        const y = horses[i].pos.y;
        // console.log(x, y);
        if(occupied[x][y]){
            horses[i].Mount(horses[occupied[x][y]])
        } else {
            occupied[x][y] = i;
        }
    }
    console.log('---------------------------')
    console.log(map);
    console.log(occupied);
    console.log('---------------------------')
}

function solve(lines){
    processInput(lines);
    let stepCount = -1;
    while(stepCount++ < MAX_COUNT){
        // console.log("stepCount: ", stepCount);
        // console.log(horses);
        // console.log(occupied);
        for(let i =0; i < horses.length; i++){
            const count = horses[i].countHorses();
            if(count >= 4){
                return stepCount;
            }
        }
        for(let i = 0; i < horses.length; i++){
            const currentHorse = horses[i];
            let x = currentHorse.pos.x;
            let y = currentHorse.pos.y;
            occupied[x][y] = undefined;
            currentHorse.nextMove();
            x = currentHorse.pos.x;
            y = currentHorse.pos.y;
            if(occupied[x][y]){
                currentHorse.Mount(horses[occupied[x][y]]);
            } else{
                occupied[x][y] = i;
            }
        }
    }
    return stepCount;
}


const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./17780.txt";
let inputs = fs.readFileSync(filePath).toString().split("\n");
// let inputs = [
//     '4 4',     '0 0 0 0',
//     '0 0 0 0', '0 0 0 0',
//     '0 0 0 0', '1 1 1',
//     '1 2 1',   '1 3 1',
//     '2 4 3'
//   ]
// let inputs = [
    // '4 4',     '0 0 2 0',
//     '0 0 1 0', '0 0 1 2',
//     '0 2 0 0', '2 1 1',
//     '3 2 3',   '2 2 1',
//     '4 1 2'
//   ]
console.log(inputs);
const result = solve(inputs);
console.log(result)
