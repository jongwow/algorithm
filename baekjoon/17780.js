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
        let nextPosition = new Pos(this.pos.x + this.dir.x, this.pos.y + this.dir.y, this.pos.n)
        if(nextPosition.IsOutOfWall()){
            firstMove === true && this._moveNextBlue();
        } else {
            const nextTile = map[nextPosition.x][nextPosition.y];
            if(nextTile === COLOR.BLUE){
                firstMove === true && this._moveNextBlue();
            } else if(nextTile === COLOR.RED){
                this._moveNextRed(nextPosition);
            } else if(nextTile === COLOR.WHITE){
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
        this.reverseHorses(nextPosition);
    }
    _moveNextWhite(nextPos){
        let currentHorse = this;
        while(currentHorse){
            currentHorse.pos = nextPos;
            currentHorse = currentHorse.nextHorse;
        }
    }
    reverseHorses(nextPosition){
        // traverseHorse
        let previousHorse = undefined;
        let nextHorse = undefined;
        let currentHorse = this;
        while(currentHorse){
            currentHorse.pos = nextPosition;
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
        if(this.movable === false){
            return 1;
        }
        let count = 1;
        let nextHorse = this.nextHorse;
        while(nextHorse){
            count++;
            nextHorse = nextHorse.nextHorse;
        }
        return count;
    }
}
const map = [];
const occupied = [];
const horses = [];
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
        const x = horses[i].pos.x;
        const y = horses[i].pos.y;
        occupied[x][y] = i;
    }
}

function solve(lines){
    processInput(lines);
    let stepCount = -1;
    
    while(stepCount++ < MAX_COUNT){
        for(let i = 0; i < horses.length; i++){
            const count = horses[i].countHorses();
            if(count >= 4){
                return stepCount;
            }
        }
        
        for(let i = 0; i < horses.length; i++){
            const currentHorse = horses[i];
            if(currentHorse.movable === false){
                continue;
            }
            let x = currentHorse.pos.x;
            let y = currentHorse.pos.y;
            occupied[x][y] = undefined;
            currentHorse.nextMove();
            x = currentHorse.pos.x;
            y = currentHorse.pos.y;
            if(occupied[x][y]){
                const count = currentHorse.Mount(horses[occupied[x][y]]);
                console.log(count)
                // if(count >= 4){
                //     return stepCount;
                // }
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
// const inputs = [
//     '6 10',        '0 1 2 0 1 1',
//     '1 2 0 1 1 0', '2 1 0 1 1 0',
//     '1 0 1 1 0 2', '2 0 1 2 0 1',
//     '0 2 1 0 2 1', '1 1 1',
//     '2 2 2',       '3 3 4',
//     '4 4 1',       '5 5 3',
//     '6 6 2',       '1 6 3',
//     '6 1 2',       '2 4 3',
//     '4 2 1'
//   ]
console.log(inputs);
const result = solve(inputs);
if(result > MAX_COUNT){
    console.log(-1);
} else {
    console.log(result)
}
