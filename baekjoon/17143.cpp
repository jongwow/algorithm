//
// Created by Jongwoo on 2020-03-15.
//
#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#define ll long long

using namespace std;

struct shark {
    int r, c, s, d, z;
};

//(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
int R, C, M; // 2<= R,C <= 100, 0<=M<=RxC
int sea[101][101][2]; //[r][c]. shark의 번호를 넣어주면 됨
int r, c, s, d, z; // (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000)
int dr[5] = {0, -1, 1, 0, 0};
int dc[5] = {0, 0, 0,1, -1};
vector<shark> sharks;

void input() {
    memset(sea, -1, sizeof(sea));
    cin >> R >> C >> M;
    for (int i = 0; i < M; i++) {
        cin >> r >> c >> s >> d >> z;
        if(sea[r][c][0] != -1){
            if(sharks[sea[r][c][0]].z < z){
                sharks[sea[r][c][0]].d = 0;
                sea[r][c][0] = i;
            }else{
                d = 0;
            }
        }
        sharks.push_back(shark{r, c, s, d, z});
        sea[r][c][0] = i;
    }
}

// 낚시꾼의 위치에서 가장 위에 있는 물고기 잡기
int fish(int c, int state) {
    int ret=0;
    for(int i=1; i<=R; i++){
        if(sea[i][c][state] != -1){
            ret = sharks[sea[i][c][state]].z; // 값 더하고
            sharks[sea[i][c][state]].d = 0;//죽이고
            sea[i][c][state] = -1; //지도에서 없애고
            break;
        }
    }
    return ret;
}

int flip(int d){
    switch(d){//상하우좌
        case 1:
            return 2;
        case 2:
            return 1;
        case 3:
            return 4;
        case 4:
            return 3;
        default:
            cout << "ERR" << endl;
            return 0;
    }
}
// 상어 한머리 움직이기
void moveShark(int idx, int state) {
    cout << "(" << idx << ", " << state << ")" << endl;
    if (sharks[idx].d == 0) { //이미 죽은 상어
        //밖으로 빼낼 수도 있겠다.
        return;
    } else {
        int newState = state == 0 ? 1 : 0;
        //상어 움직이기.
        //기존의 shark가 위치한 sea의 값을 -1으로 바꿔주기 =>
        sea[sharks[idx].r][sharks[idx].c][state] = -1;

        //shark의 값을 바꿔주기. 위치, state 등
        int newR = sharks[idx].r + dr[sharks[idx].d] * sharks[idx].s;
        int newC = sharks[idx].c + dc[sharks[idx].d] * sharks[idx].s;

        while(!(1 <=newR && newR <= R && 1<= newC && newC<=C)){
            if(newR <= 0){
                newR = 2 - newR;
                sharks[idx].d = flip(sharks[idx].d);
            }
            if(newC <= 0){
                newC = 2 - newC;
                sharks[idx].d = flip(sharks[idx].d);
            }
            if(newR > R){
                newR = 2*R - newR;
                sharks[idx].d = flip(sharks[idx].d);
            }
            if(newC > C){
                newC = 2*C - newC;
                sharks[idx].d = flip(sharks[idx].d);
            }
        }

        sharks[idx].r = newR;
        sharks[idx].c = newC;

        //sea에 shark가 존재하는지 확인하기.
        if (sea[sharks[idx].r][sharks[idx].c][newState] == -1) {
            //sea에 shark가 존재하지 않는다면
            // 그대로 넣어주기
            sea[sharks[idx].r][sharks[idx].c][newState] = idx;
        } else {
            //기존의 그것이 크다면
            if (sharks[sea[sharks[idx].r][sharks[idx].c][newState]].z > sharks[idx].z) {
                //지금것 죽이기
                sharks[idx].d = 0;
            } else {
                //기존것 죽이고
                //지금것 넣기
                sharks[sea[sharks[idx].r][sharks[idx].c][newState]].d = 0;
                sea[sharks[idx].r][sharks[idx].c][newState] = idx;
            }
        }
    }
}

// 아래 반복
//  사냥꾼 움직이기
//  잡기
//  state를 바꿔서
//  상어 이동시키기

void printSea(int state){
    for(int i=1; i<=R; i++){
        for (int j=1; j<=C; j++){
            cout << sea[i][j][state] << " ";
        }
        cout << endl;
    }
}

ll solve(){
    ll res=0;
    int state=0;
    for(int i=1; i<=C; i++){
        res += fish(i, state);
        for(int j=0; j<sharks.size(); j++){
            moveShark(j, state);
        }
        state = state == 0 ? 1:0;
    }
    return res;
}

int main() {
    // sea만 (0,0)이 아닌 (1,1)부터 시작!
    freopen("../input/17143.txt", "r", stdin);
    input();
    cout  << solve() << endl;
    return 0;
}