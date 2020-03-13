//
// Created by Jongwoo on 2020-03-12.
//
#include <iostream>
using namespace std;
int N;
int cols[100];

bool promising(int level){
    for(int i=1; i<level; i++){
        if(cols[level] == cols[i])
            return false;
        if(true){ // 같은 대각선에 있는지 유무 확인

        }
    }
    return true;
}
bool queens(int level){
    if(!promising(level)){
        return false;
    }else if (level == N)
        return true;
    for(int i=1; i<=N; i++){
        cols[level+1]= i;
        if(queens(level+1))
            return true;
    }
    return false;
}
