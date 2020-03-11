//
// Created by Jongwoo on 2020-03-12.
//
#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

vector<vector<int>> board;

int aaa[4][3][2] = {{{0, 0}, {1, 0}, {1, -1}},
                    {{0, 0}, {1, 0}, {1, 1}},
                    {{0, 0}, {0, 1}, {1, 0}},
                    {{0, 0}, {0, 1}, {1, 1}}};

bool set(vector<vector<int>> &board, int y, int x, int shape, int delta) {
    // 경계선 내부인지 확인
    bool res = true;
    for (int i = 0; i < 3; i++) {
        int nextY = y + aaa[shape][i][0];
        int nextX = x + aaa[shape][i][1];
        if (0 > nextX || nextX >= board[0].size() || 0 > nextY || nextY >= board.size())
            res = false;
        else if ((board[nextY][nextX] += delta) > 1)
            res = false;
    }
    return res;
}

int cover(vector<vector<int>> &board) {
    int y = -1;
    int x = -1;
    for(int i=0; i<board.size(); i++){
        for(int j=0; j<board[i].size(); j++)
            if(board[i][j] == 0){
                y = i;
                x = j;
                break;
            }
        if(y != -1) break;
    }
    if(y == -1) return 1;
    int ret= 0;
    for(int type = 0; type<4; type++){
        if(set(board, y, x, type, 1))
            ret += cover(board);
        set(board, y, x, type, -1);
    }
    return ret;
}

int main() {
    freopen("../algospot/algospotInput.txt", "r", stdin);
    int tc;
    int h = 0, w = 0;
    cin >> tc;
    while (tc-- > 0) {
        cin >> h >> w;
        board = vector<vector<int>>(h, vector<int>(w, -1));
        for (int i = 0; i < h; i++) {
            char ch;
            for (int j = 0; j < w; j++) {
                cin >> ch;
                if (ch == '.')
                    board[i][j] = 0;
                else if (ch == '#')
                    board[i][j] = 1;
            }
        }

        cout << cover(board) << endl;

    }
    return 0;
}