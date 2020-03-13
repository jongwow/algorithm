//
// Created by Jongwoo on 2020-03-10.
//
#include <iostream>
#include <string.h>
using namespace std;

int n, board[100][100];
bool jump(int y, int x){
    //base Case
    if(y >= n || x >= n) return false;
    if(y == n-1 && x == n-1) return true;
    int jS = board[y][x];
    return jump(y+jS, x) || jump(y, x+jS);
}

bool myJump(int y, int x){
    if(y >= n || x>= n) return false;
    if(y == n-1 && x == n-1) return true;
    int js = board[y][x];
    return myJump(y+js, x) || myJump(y, x+js)
}

int cache[100][100];

int jump2(int y, int x){
    if(y >= n || x >= n) return 0;
    if(y == n-1 && x == n-1) return 1;

    int& ret=cache[y][x];
    if(ret != -1) return ret;
    int js = board[y][x];
    ret = (jump2(y+js, x) || jump2(y, x+js));
    return ret;
}

int jump2(int y, int x){
    if(y >= n || x >= n ) return 0;
    if(y == n-1 && x == n-1) return 1;
    int& ret = cache[y][x];
    if(ret != -1) return ret;
    int js = board[y][x];
    ret= (jump2(y+js, x) || jump2(y, x+js));
    return ret;
}

int main(){

}
