function solve(map, N, M){
//  console.log(map, N, M);
  const dx = [0, -1, 0, 1];
  const dy = [1, 0, -1, 0];
  const Q = [];
  const visited = {};
  visited[0] = {};
  visited[0][0] = 1;
  Q.push({x: 0, y: 0});
  while(Q.length !== 0){
 //   console.log(Q);
    const cur = Q.shift();
    if(cur.x === N-1 && cur.y === M-1){
      return visited[cur.x][cur.y];
    } 
  //  console.log(cur);
    for(let i=0; i<4; i++){
      let nX = dx[i]+cur.x;
      let nY = dy[i]+cur.y;
      if(0 <= nX && nX < N&& 0 <= nY && nY < M){
        if(visited[nX] && visited[nX][nY]){
          // nothing
        }else if (map[nX][nY] === '1'){
          if(!visited[nX]){
           visited[nX] = {};
          }
          visited[nX][nY] = visited[cur.x][cur.y] + 1;
          Q.push({x:nX, y: nY});
        }
      }
    }
  }  
  return 0;
}

function main(){
  let fs = require('fs');
  let input = fs.readFileSync('./2178_input.txt').toString().split('\n');
  const nm = input[0].split(' ');
  const N = parseInt(nm[0]);
  const M = parseInt(nm[1]);

  //console.log(N, M);
 // console.log(input.length);
  const map = input.slice(1, N+1);
  const result = solve(map, N, M);
  return result;
}

const a = main();
console.log('---');
console.log(a);

/*
const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    rl.close();
  }

  process.exit();
})();
*/
