#include <iostream>
using namespace std;
int DP[31][31];
//겹쳐질 수 없다는 조건!!!
int bridge(int n, int m){
	if (n == 1)
		return m;
	if (DP[n][m] != -1)
		return DP[n][m];
	DP[n][m] = bridge(n - 1, m - 1) * m;
	return DP[n][m];
}

int main() {
	int tc;
	for (int i = 0; i < 31; i++)
		for (int j = 0; j < 31; j++)
			DP[i][j] = -1;
	cin >> tc;
	while (tc--) {
		int n, m;
		cin >> n >> m;
		cout << bridge(n, m) << endl;
	}
	return 0;
}