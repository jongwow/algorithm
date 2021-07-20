#include <iostream>
#include <queue>
#include <string>

using namespace std;

struct VERTEX{
  int x, y;
};

int N, M;
char map[111][111];
int visited[111][111] = {-1}; //TODO: Is this right initialization?
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

bool safe(int x, int y){
  return (0 <= x && x < 100) & (0 <= y && y < 100);
}

int solve(){
  int result = 0;
  queue<VERTEX> Q;
  Q.push((VERTEX){0, 0}); // starting point
  visited[0][0] = 1;
  while(!Q.empty()){
    VERTEX cur = Q.front();
    // check baseCase
    if(cur.x == N-1 && cur.y == M-1){
      // Since BFS, always result is a shortest path
      result = visited[cur.x][cur.y];
      return result;
    }

    // push next vertex
    for(int i=0; i<4; i++){
      int nextX = dx[i]+cur.x;
      int nextY = dy[i]+cur.y;
      if(safe(nextX, nextY) && map[nextX][nextY] == '1' && visited[nextX][nextY] == -1){
        Q.push((VERTEX){nextX, nextY});
        visited[nextX][nextY] = visited[cur.x][cur.y]+1; //TODO: Check visited toggle is here or outside of for loop
      }
    }
    Q.pop();
  }
  return result;
}

int main(){
  // Initial 
  memset(visited, -1, sizeof(visited));

  freopen("2178_input.txt", "r", stdin);
  cin >> N >> M;
  for(int i=0; i<N; i++){
    cin >> map[i];
  }
  int result = solve();
  cout << result << endl;
  return 0;
}
