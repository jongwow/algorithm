#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct VERTEX {
  int i, j;
};

char map[20][20];
int colorCount[26];
int dirI[4] = {0, 0, 1, -1};
int dirJ[4] = {1, -1, 0, 0};
int visited[20][20];

void printVisited(int N) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cout << visited[i][j];
    }
    cout << endl;
  }
}

void printMap(int N) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cout << map[i][j];
    }
    cout << endl;
  }
}

bool isInBoundary(int i, int j, VERTEX low, VERTEX high) {
  if (i < low.i || j < low.j || i >= high.i || j >= high.j) {
    return false;
  }
  return true;
}
void windowMap() {}
void checkPCL() {}
void bfs(int initialI, int initialJ, VERTEX low, VERTEX high) {
  queue<VERTEX> Q;
  char color = map[initialI][initialJ];
  Q.push((VERTEX){initialI, initialJ});
  visited[initialI][initialJ] = 1;
  while (!Q.empty()) {
    VERTEX current = Q.front();
    // check base
    Q.pop();
    for (int dir = 0; dir < 4; dir++) {
      int nextI = current.i + dirI[dir];
      int nextJ = current.j + dirJ[dir];
      if (isInBoundary(nextI, nextJ, low, high) && visited[nextI][nextJ] == 0 &&
          map[nextI][nextJ] == color) {
        visited[nextI][nextJ] = 1;
        Q.push((VERTEX){nextI, nextJ});
      }
    }
  }
  //   printVisited(N);
}
// 포함관계가 아닌 leftUp, rightDown 2쌍을 선택하는 경우의 수에 대해서?
// -> N^3

void iterateBFS(int N) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (visited[i][j] == 0) {
        char color = map[i][j];
        colorCount[color - 'A']++;
        bfs(i, j, VERTEX{0, 0}, VERTEX{N, N});
      }
    }
  }
  for (int i = 0; i < 26; i++) {
    if (colorCount[i] != 0) {
      cout << char(i + 'A') << ": " << colorCount[i] << endl;
    }
  }
}

int main() {
  freopen("./14529.txt", "r", stdin);
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> map[i][j];
    }
  }

  printMap(N);
  cout << endl;
  iterateBFS(N);
}
