#include <string.h>

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct VERTEX {
  int i, j;
};

char map[20][20];
int mapCount[20][20];
int colorCount[26];
int dirI[4] = {0, 0, 1, -1};
int dirJ[4] = {1, -1, 0, 0};
int visited[20][20];

bool isInBox(VERTEX outLow, VERTEX outHigh, VERTEX inLow, VERTEX inHigh) {
  if (outLow.i <= inLow.i && outLow.j <= inLow.j && outHigh.i >= inHigh.i &&
      outHigh.j >= inHigh.j) {
    return true;
  }
  return false;
}
void printVisited(VERTEX low, VERTEX high) {
  for (int i = low.i; i < high.i; i++) {
    for (int j = low.i; j < high.j; j++) {
      cout << visited[i][j] << " ";
    }
    cout << endl;
  }
}

void printMapCount(int N) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cout << mapCount[i][j];
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
  if (i < low.i || j < low.j || i > high.i || j > high.j) {
    return false;
  }
  return true;
}
void windowMap() {}
void checkPCL() {}
int bfs(int initialI, int initialJ, VERTEX low, VERTEX high) {
  int count = 0;
  if (visited[initialI][initialJ] == 1) {
    return count;
  }
  queue<VERTEX> Q;
  char color = map[initialI][initialJ];
  Q.push((VERTEX){initialI, initialJ});
  visited[initialI][initialJ] = 1;
  while (!Q.empty()) {
    VERTEX current = Q.front();
    count++;
    // check base
    Q.pop();
    for (int dir = 0; dir < 4; dir++) {
      int nextI = current.i + dirI[dir];
      int nextJ = current.j + dirJ[dir];
      if (isInBoundary(nextI, nextJ, low, high) && visited[nextI][nextJ] != 1 &&
          map[nextI][nextJ] == color) {
        visited[nextI][nextJ] = 1;
        Q.push((VERTEX){nextI, nextJ});
      }
    }
  }
  return count;
  //   printVisited(N);
}
// 포함관계가 아닌 leftUp, rightDown 2쌍을 선택하는 경우의 수에 대해서?
// -> N^3
// 2개의 색상
// 한 색상은 한개의 지역만
// 다른 색상은 두개 이상의 지역을

void iterateBFS(int N) {
  vector<VERTEX> answers;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      // select InitialPoint
      VERTEX low = VERTEX{i, j};
      for (int ii = i; ii < N; ii++) {
        for (int jj = j; jj < N; jj++) {
          // select endPoint
          VERTEX high = VERTEX{ii, jj};

          for (int iii = low.i; iii <= high.i; iii++) {
            for (int jjj = low.j; jjj <= high.j; jjj++) {
              char color = map[iii][jjj];
              int cnt = bfs(iii, jjj, low, high);
              if (cnt > 0) {
                colorCount[color - 'A']++;
              }
            }
          }
          // printVisited(low, high);
          int uniqueColor = 0;
          bool flag = true;
          int conditionOne = false;
          int conditionTwo = false;

          for (int cIndex = 0; cIndex < 26; cIndex++) {
            if (colorCount[cIndex] > 0) {
              uniqueColor++;
            }
            if (uniqueColor > 2) {
              flag = false;
              break;
            }
            if (colorCount[cIndex] == 1) {
              conditionOne = true;
            }
            if (colorCount[cIndex] >= 2) {
              conditionTwo = true;
            }
          }
          if (conditionOne && conditionTwo && flag) {
            cout << "FOUND:"
                 << "(" << low.i << ", " << low.j << ")(" << high.i << ", "
                 << high.j << ")" << endl;

            // for (int cIndex = 0; cIndex < 26; cIndex++) {
            //   if (colorCount[cIndex] != 0) {
            //     cout << char(cIndex + 'A') << ": " << colorCount[cIndex]
            //          << endl;
            //   }
            // }
            answers.push_back(low);
            answers.push_back(high);
          }
          memset(colorCount, 0, sizeof(colorCount));
          memset(visited, 0, sizeof(visited));
        }
      }
    }
  }

  for (int i = 0; i < answers.size(); i += 2) {
    VERTEX low = answers[i];
    VERTEX high = answers[i + 1];
    bool isResult = true;
    for (int nI = 0; nI < answers.size(); nI += 2) {
      if (i == nI) {
        continue;
      }
      VERTEX nLow = answers[nI];
      VERTEX nHigh = answers[nI + 1];
      if (isInBox(nLow, nHigh, low, high)) {
        isResult = false;
        break;
      }
    }
    if (isResult) {
      cout << "REALLY FOUND:"
           << "(" << low.i << ", " << low.j << ")(" << high.i << ", " << high.j
           << ")" << endl;
    }
  }
  // int result = 0;
  // for (int i = 0; i < answers.size(); i += 2) {
  //   bool outFlag = false;
  //   VERTEX low = answers[i];
  //   VERTEX high = answers[i + 1];
  //   for (int mI = low.i; mI <= high.i; mI++) {
  //     for (int mJ = low.j; mJ <= high.j; mJ++) {
  //       if (mapCount[mI][mJ] == 1) {
  //         result++;
  //         outFlag = true;
  //         break;
  //       }
  //     }
  //     if (outFlag) {
  //       break;
  //     }
  //   }
  // }
  // printMapCount(N);
  // cout << result << endl;
  // for (int i = 0; i < 26; i++) {
  //   if (colorCount[i] != 0) {
  //     cout << char(i + 'A') << ": " << colorCount[i] << endl;
  //   }
  // }
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
  // cout << isInBox(VERTEX{0, 0}, VERTEX{3, 2}, VERTEX{0, 0}, VERTEX{2, 1})
  //      << endl;
  iterateBFS(N);
}
