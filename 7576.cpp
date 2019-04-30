#include <iostream>
#include <queue>
using namespace std;
struct VERTEX {
	int n, m,day;
};
int dn[4] = { 0,0,1,-1 };
int dm[4] = { 1,-1,0,0 };
int box[1001][1001];//box[n][m]
int M, N;
bool safe(int n, int m) {
	return (0 <= n && n < N) && (0 <= m && m < M);
}
int main() {
	cin >> M >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			cin >> box[i][j];
		}
	queue<VERTEX> Q;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			if (box[i][j] == 1)
				Q.push(VERTEX{ i, j, 1});
		}
	while (!Q.empty()) {
		VERTEX cur = Q.front();
		Q.pop();
		for (int i = 0; i < 4; i++) {
			if (safe(cur.n + dn[i], cur.m + dm[i]) && box[cur.n + dn[i]][cur.m + dm[i]] == 0) {
				box[cur.n + dn[i]][cur.m + dm[i]] = cur.day + 1;
				Q.push(VERTEX{ cur.n + dn[i], cur.m + dm[i], cur.day + 1 });
			}
		}
	}
	int res = -1;
	int flag = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (box[i][j] > res)
				res = box[i][j];
			if (box[i][j] == 0) {
				res = 0;
				flag = 1;
				break;
			}
		}
		if (flag)
			break;
	}
	cout << res-1 << endl;
}