//
// Created by Jongwoo on 2020-03-10.
//
#include <iostream>
#include <stdio.h>

using namespace std;
/*
 * 문제를 읽고 이해한다.
 *  각자를 자신과 친구인 학생과 묶음.
 *  모든 학생이 묶임
 * 문제를 익숙한 용어로 재정의
 * 학생관계 = friends[N][N]
 * 짝유무 =  paired[N]
 *  모든 학생이 짝 있음
 *      return true
 *
 *  친구관계 == 1 : 짝 가능
 *      짝짓고 다음인간으로
 *      짝해제 다음인간으로
 *  else: 짝 불가능
 *      return false
 * 어떻게 해결할지 계획
 *  base Case:
 *      모든 학생이 묶임 return true
 *      해당 학생이 짝 불가능 return false
 *  짝 가능한 친구와 짝맺음
 *  다음 학생으로 넘어가기
 *  짝 맺은 친구와 절교
 *  다음 학생으로 넘어가기
 * 계획 검증
 * 프로그램 구현
 * 회고
 * */
bool paired[10];
int friends[10][10];
int N;

int cnt = 0;

bool countPairings(int k) {
    if (k == N) {
        cnt++;
        return true;
    }
    if (paired[k])
        return countPairings(k + 1);
    int l;
    for (l = k + 1; l < N; l++) {
        if (friends[k][l] && !paired[l]) {
            paired[l] = paired[k] = true;
            countPairings(k + 1);
            paired[l] = paired[k] = false;
        }
    }
    return false;
}
int n=0;
int countP(bool taken[10]) {
    bool finished = true;
    for (int i = 0; i < n; i++) if (!taken[i]) finished = false;
    if (finished) return 1;
    int ret = 0;
    for (int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(!taken[i] && !taken[j] && friends[i][j]){
                taken[i] = taken[j] = true;
                ret += countP(taken);
                taken[i] = taken[j] = false;
            }
        }
    }
    return ret;
}

int countP2(bool taken[10]){
    int firstFreeStudent = -1;
    for(int i=0; i<n; i++){
        if(!taken[i]){
            firstFreeStudent = i;
            break;
        }
    }

    if(firstFreeStudent == -1) return 1;

    int ret = 0;
    for(int first = firstFreeStudent+1; first< n; first++){
        if(!taken[first] && friends[firstFreeStudent][first]){
            taken[first] = taken[firstFreeStudent] = true;
            ret += countP2(taken);
            taken[first] = taken[firstFreeStudent] = false;
        }
    }
    return ret;
}

int main() {
    freopen("../algospot/algospotInput.txt", "r", stdin);
    int tc;
    cin >> tc;
    while (tc-- > 0) {
        cin >> N;
        int m, a, b;
        cin >> m;
        for (int i = 0; i < m; i++) {
            cin >> a >> b;
            friends[a][b] = friends[b][a] = 1;
        }
        cnt = 0;
        countPairings(0);
        cout << cnt << endl;
    }
}