//
// Created by Jongwoo on 2020-03-10.
//
#include <iostream>
#include <vector>
#include <string>

using namespace std;
/*
 * hasWord(y, x, word) 보글 게임판 (y, x)에서 시작하는 단어 word의 존재여부를 반환한다.
 * 만약 word == 0이라면 성공!
 * 만약 word와 맞지 않는다면 실패!
 * ----
 * 만약 (y,x)에 있는 글자가 원하는 단어의 첫 글자와 다를 경우 항상 실패
 * 만약 원하는 단어==한글자, 그 글자가 (y,x)일 경우 항상 성공
 * hasWord(y+d1, x+d2, word[1:])
 * */
vector<vector<char>> map;
int N;
int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

bool isRange(int y, int x) {
    return y >= 0 && y < N && 0 <= x && x < N;
}

bool hasWord(int y, int x, string &word) {
    if (!isRange(y, x)) {
        return false;
    }
    if (map[y][x] != word[0]) {
        return false;
    }
    if (word.size() == 1) {
        return true;
    }
    for (int d = 0; d < 8; d++) {
        int nY = y + dy[d], nX = x + dx[d];
        if (hasWord(nY, nX, word.substr(1))) return true;
    }
    return false;
}

int main() {
    N = 5;
    map = vector<vector<char>>(N, vector<char>(N, '.'));

}

