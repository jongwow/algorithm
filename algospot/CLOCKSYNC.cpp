//
// Created by Jongwoo on 2020-03-12.
//
#include <iostream>
#include <vector>

using namespace std;
/**
 * 1. 문제를 읽고 이해한다.
 * 우선 완전 탐색으로 한번 해보자.
2. 문제를 익숙한 용어로 재정의한다.
  int clock[16]: clock[k]는 k번째 시계의 시간을 나타낸다.
  - domain: 12, 3, 6, 9. => 0, 1, 2, 3
  vector<int> switch[10]: switch[k]는 k번째 스위치와 연결된 시계들의 배열을 나타낸다.
  - switch[0]: 0, 1, 2
  bool clicked[10][3]: switch가 눌린 횟수를 저장하는 배열.
  - switch가 4번 이상 눌리는 것을 방지하기 위한 배열이다.
  - clicked[k][n]: k번째 switch가 n번 눌렸는지 여부.
3. 어떻게 해결할지 계획을 세운다.
 ClickSwitch(switch):
    switch를 받아서 누른다.
 ClockSync(clock):
    Base Case:
        if(check12(clock)): true
        else:

4. 계획을 검증한다.
5. 프로그램으로 구현한다.
6. 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다.
 */
const int INF = 987654321, SWITCHES = 10, CLOCKS = 16;
char aaa[5] = "12345";
const char linked[SWITCHES][CLOCKS + 1] = {
        //   0123456789012345
        "xxx.............",
        "...x...x.x.x....",
        "....x.....x...xx",
        "x...xxxx........",
        "......xxx.x.x...",
        "x.x...........xx",
        "...x..........xx",
        "....xx.x......xx",
        ".xxxxx..........",
        "...xxx...x...x..",
};

bool areAligned(const vector<int> &clocks) {
    for (int i = 0; i < CLOCKS; i++) {
        if (clocks[i] != 12)
            return false;
    }
    return true;
}

void pushSwitch(vector<int> &clocks, int switchN) {
    for (int i = 0; i < CLOCKS; i++) {
        if (linked[switchN][i] == 'x') {
            clocks[i] += 3;
            if (clocks[i] == 15) clocks[i] = 3;
        }
    }
}

int solve(vector<int> &clocks, int switchN) {
    if (switchN == SWITCHES) return areAligned(clocks) ? 0 : INF;
    int ret = INF;
    for(int cnt=0; cnt<4; cnt++){
        ret = min(ret, cnt+solve(clocks, switchN+1));
        pushSwitch(clocks, switchN);
    }
    return ret;
}