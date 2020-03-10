#include <iostream>
#include <queue>
using namespace std;

struct TOMATO{
	int m, n, h, day;
};
int M, N, H; 
int box[100][100][100];//[M][N][H]
int dm[6] = { -1, 1, 0, 0, 0, 0};
int dn[6] = {0, 0, -1, 1, 0, 0};
int dh[6] = {0, 0, 0, 0, -1, 1};

bool boundary(int m, int n, int h) {
	return (0 <= m && m < M && 0 <= n && n < N && 0 <= h && h < H) && (box[m][n][h] == 0);
}

int main() {
	cin >> M >> N >> H;
	for (int hI = 0; hI < H; hI++) {
		for (int nI = 0; nI < N; nI++) {
			for (int mI = 0; mI < M; mI++) {
				cin >> box[mI][nI][hI];
			}
		}
	}
	queue<TOMATO> Q;
	for (int hI = 0; hI < H; hI++) {
		for (int nI = 0; nI < N; nI++) {
			for (int mI = 0; mI < M; mI++) {
				if (box[mI][nI][hI] == 1) {
					Q.push(TOMATO{mI, nI, hI, 1 });// 0번째 day에 이미 익은 토마토를 큐에 넣는다.
				}
			}
		}
	}
	while (!Q.empty()) { //Q가 비어있지 않을 때 == 빌때까지.
		TOMATO cur = Q.front();
		Q.pop();
		//6방위에 대해서
		for (int i = 0; i < 6; i++) {
			//다음 갈 수 있는 토마토에 대해서
			//벽에 닿지 않을 때 && 토마토가 존재할 때 && 토마토가 익지 않았을 때
			if (boundary(cur.m + dm[i], cur.n + dn[i], cur.h + dh[i])) {
				TOMATO nxT = TOMATO{ cur.m + dm[i], cur.n + dn[i], cur.h + dh[i], cur.day + 1 };
				box[nxT.m][nxT.n][nxT.h] = nxT.day;
				Q.push(nxT);
			}
		}
	}
	/*
	for (int hI = 0; hI < H; hI++) {
		for (int nI = 0; nI < N; nI++) {
			for (int mI = 0; mI < M; mI++) {
				cout << box[mI][nI][hI];
			}
			cout << endl;
		}
		cout << endl;
	}*/
	int days = -1;
	int flag = 0;
	for (int hI = 0; hI < H; hI++) {
		for (int nI = 0; nI < N; nI++) {
			for (int mI = 0; mI < M; mI++) {
				if (box[mI][nI][hI] == 0) {
					flag = 1;
					break;
				}
				if (box[mI][nI][hI] > days)
					days = box[mI][nI][hI];
			}
			if (flag == 1)
				break;
		}
		if (flag == 1)
			break;
	}
	if(flag == 1)
		days = 0;
	cout << "RESULT : ";
	cout << days -1<< endl;
	return 0;
}