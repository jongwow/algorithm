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

bool putOn(vector<vector<int>> &board, int y, int x, int type, int delta) {
    bool res = true;
    for (int i = 0; i < 3; i++) {
        int nY = y + aaa[type][i][0];
        int nX = x + aaa[type][i][1];
        if (0 > nX || 0 > nY || board[0].size() <= nX || board.size() <= nY)
            res = false;
        else if ((board[nY][nX] += delta) > 1)
            res = false;
    }
    return res;
}

int coverTile(vector<vector<int>> &board) {
    // 가장 첫번쨰 왼쪽 위 빈 타일을 찾는 부분
    int y = -1;
    int x = -1;
    for (int h = 0; h < board.size(); h++) {
        for (int w = 0; w < board[0].size(); w++) {
            if (board[h][w] == 0) {
                y = h;
                x = w;
                break;
            }
        }
        if (y != -1)
            break;
    }
    //기저사례
    if (y == -1) return 1;
    int ret = 0;
    for (int type = 0; type < 4; type++) {
        if (putOn(board, y, x, type, 1))
            ret += coverTile(board);
        putOn(board, y, x, type, -1);
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

        cout << coverTile(board) << endl;

    }
    return 0;
}