#include <iostream>
#include <algorithm>

#define INF 987654321
using namespace std;

int dp[301][2];
int stair[301];
int height;

int solve(int st, int state) {
    if (st == height - 1)
        return stair[st];
    if (st >= height)
        return -INF;
    if (dp[st][state] != 0)
        return dp[st][state];
    if (state == 0)
        dp[st][state] = max(solve(st + 1, 1), solve(st + 2, 0)) + stair[st];
    else
        dp[st][state] = solve(st + 2, 0) + stair[st];
    return dp[st][state];
}

int main() {
    cin >> height;
    for (int i = 0; i < height; i++) {
        cin >> stair[i];
    }
    cout << max(solve(0, 0), solve(1, 0)) << endl;
}