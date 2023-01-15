const COLOR = {
    BLUE: 2,
    RED: 1,
    WHITE: 0,
    WALL: 4,
};
class Pos {
    constructor(x, y, n){
        this.x = x;
        this.y = y;
        this.n = n;
    }
    IsOutOfWall(){
        if(this.x >= this.n || this.y >= this.n || this.x < 0 || this.y < 0) return true;
        return false;
    }
}
/**
 * x,y
 */
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
            this.x = 1;
            this.y = 0;
        }
        else if(dir === 4){
            this.x = 0;
            this.y = 1;
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
    constructor(position, direction){
        this.pos = position;
        this.dir = direction;
        this.horses = [this];
    }
    nextMove(firstMove = true){
        let nextPosition = new Pos(this.pos.x + this.dir.x, this.pos.y + this.dir.y, this.pos.n)
        if(nextPosition.IsOutOfWall()){
            firstMove === true && this._moveNextBlue();
        } else {
            const nextTile = map[nextPosition.x][nextPosition.y];
            if(nextTile.color === COLOR.BLUE){
                firstMove === true && this._moveNextBlue();
            }
            if(nextTile.color === COLOR.RED){
                this._moveNextRed(nextPosition);
            }
            if(nextTile.color === COLOR.WHITE){
                this._moveNextWhite(nextPosition);
            }
        }
    }
    Mount(bottom){
        bottom.horses.push(this);
    }
    _moveNextBlue(){
       this.dir.reverse();
       this.nextMove(false);
    }
    _moveNextRed(){
        this.reverseHorses();
        this.horses.forEach(horse => {
            horse.pos = nextPos;
       });
    }
    _moveNextWhite(nextPos){
       this.horses.forEach(horse => {
            horse.pos = nextPos;
       });
    }
    reverseHorses(){
        this.horses.forEach(horse => {
            horse.reverseHorses();
        })
        this.horses.reverse();
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
        horses.push(new OldHorse(new Pos(x-1, y-1, N-1), new Dir(dir)));
    }
    console.log('---------------------------')
    console.log(map);
    console.log(occupied);
    console.log('---------------------------')
}

function solve(lines){
    processInput(lines);
    let stepCount = 0;
    while(stepCount++ < 1000){
        // console.log("stepCount: ", stepCount);
        console.log(horses);
        for(let i =0; i < horses.length; i++){
            const currentHorse = horses[i];
            if(currentHorse.horses.length >= 4){
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
              horses[occupied[x][y]].Mount(currentHorse);
            } else{
              occupied[x][y] = i;
            }
        }
    }

    // const [N, K] = lines[0].split(" ").map((item) => +item); // N K
    // for(let i = 1; i <= N; i++){
    //     const mapData = lines[i].split(" ").map((item) => +item);
    //     map.push(mapData);
    //     horseMap.push( new Array(N).fill(null).map(() => new Array()));
    // }
    // for(let i = N+1; i < N+1+K; i++){
    //     const [x, y, dir]= lines[i].split(" ").map((item) => +item);
    //     horses.push(new Horse(x, y, dir));
    // }
    // for(let i = 0; i < K; i++){
    //     const horse = horses[i];
    //     console.log(horse.getX(), horse.getY());
    //     horseMap[horse.getX()][horse.getY()].push(horse);
    // }
    // let stepCount = 0;
    // while(stepCount++ < 1000){
    //     for(let i = 0; i < N; i++){
    //         for(let j = 0; j < N; j++){
    //             if(map[i][j].length >=4 ){
    //                 break;
    //             }
    //         }
    //     }

    //     for(let i = 0; i<horses.length; i++){
    //         const horse = horses[i];
    //         const dir = horse.getDir();
    //         let nextX = horse.getX() + DIR[dir].x;
    //         let nextY = horse.getY() + DIR[dir].y;
    //         let firstMove = true;
    //         // out of wall
    //         if(nextX < 0 || nextY < 0 || nextX >= N || nextY >= N){
    //             // move blue action
    //             firstMove = false;
    //             nextX = horse.getX() - DIR[dir].x;
    //             nextY = horse.getY() - DIR[dir].y;
    //         }
    //         let nextTile = map[nextX][nextY];
    //         if(firstMove && nextTile === COLOR.BLUE){
    //             firstMove = false;
    //             nextX = horse.getX() - DIR[dir].x;
    //             nextY = horse.getY() - DIR[dir].y;
    //         }
    //         if(nextTile === COLOR.RED){

    //         }
    //         if(nextTile === COLOR.WHITE){

    //         }
    //         horse.move()
    //     }
    // }

    // // console.log(horseMap[0][1].push(1));
    // printMap(horseMap);
}
const DIR = {
    1: {x: 0, y: 1},
    2: {x: 0, y: -1},
    3: {x: 1, y: 0},
    4: {x: -1, y: 0},
}


const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./17780.txt";
let inputs = fs.readFileSync(filePath).toString().split("\n");
solve(inputs);