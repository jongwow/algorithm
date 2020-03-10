#include <iostream>
#include <algorithm>
using namespace std;
int dp[500][500];
int tri[500][500];
int n;
int triangle(int a, int b) {
	if (a == n)
		return 0;
	if (dp[a][b] != -1)
		return dp[a][b];
	dp[a][b] = max(triangle(a + 1, b + 1) + tri[a][b], triangle(a + 1, b) + tri[a][b]);
	return dp[a][b];
}

int main() {
	for (int i = 0; i < 500; i++) {
		for (int j = 0; j < 500; j++)
			dp[i][j] = -1;
	}
	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j <= i; j++)
			cin >> tri[i][j];

	cout << triangle(0, 0) << endl;
	return 0;
}