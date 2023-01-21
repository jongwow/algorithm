#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// S: 학생, T: 선생, X: 아무것도 없다.

char map[7][7];

struct VERTEX {
  size_t x, y;
};

vector<VERTEX> teachers;

void printMap(int N) {
  if (!(map[0][2] == 'O' && map[1][1] == 'O' && map[3][2] == 'O')) {
    return;
  }
  for (size_t i = 0; i < N; i++) {
    for (size_t j = 0; j < N; j++) {
      cout << map[i][j] << " ";
    }
    cout << endl;
  }
  return;
}
bool isSuccess(int N) {
  //   printMap(N);

  for (const auto teacher : teachers) {
    int x = teacher.x;
    int y = teacher.y;
    // cout << x << ", " << y << endl;
    for (int i = y - 1; i >= 0; i--) {
      if (map[i][x] == 'S') {
        // cout << "case1: " << map[i][x] << ", " << i << ", " << x << endl;
        return false;
      }
      if (map[i][x] == 'O') {
        break;
      }
    }

    for (int i = y + 1; i < N; i++) {
      if (map[i][x] == 'S') {
        // cout << "case2: " << map[i][x] << ", " << i << ", " << x << endl;
        return false;
      }
      if (map[i][x] == 'O') {
        break;
      }
    }

    for (int i = x - 1; i >= 0; i--) {
      if (map[y][i] == 'S') {
        // cout << "case3: " << map[y][i] << ", " << y << ", " << i << endl;
        return false;
      }
      if (map[y][i] == 'O') {
        break;
      }
    }
    for (int i = x + 1; i < N; i++) {
      if (map[y][i] == 'S') {
        // cout << "case4: " << map[y][i] << ", " << y << ", " << i << endl;
        return false;
      }
      if (map[y][i] == 'O') {
        break;
      }
    }
  }
  return true;
}

/*
if non-promising: failure
else if success: success
else: visit children recursively
*/
bool solve(int N, int count) {
  if (count == 3) {
    return isSuccess(N);
  } else {
    if (count == 4) {
      cout << "count cannot be 4" << endl;
      return false;
    }

    for (size_t x = 0; x < N; x++) {
      for (size_t y = 0; y < N; y++) {
        if (map[y][x] == 'X') {
          map[y][x] = 'O';
          if (solve(N, count + 1)) {
            return true;
          }
          map[y][x] = 'X';
        }
      }
    }
    return false;
  }
}
int main() {
  freopen("./18428.txt", "r", stdin);
  int N;
  cin >> N;
  for (size_t x = 0; x < N; x++) {
    for (size_t y = 0; y < N; y++) {
      cin >> map[y][x];
      if (map[y][x] == 'T') {
        VERTEX a = VERTEX{x, y};
        teachers.push_back(a);
      }
    }
  }

  //   bool result = isSuccess(N);
  bool result = solve(N, 0);
  if (result) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  // printMap(N);
}