#include <iostream>
#define mod 10007
using namespace std;
int dp[1001];

int tiling(int n) {
	if (n == 1)
		return 1;
	if (n == 2)
		return 2;
	if (dp[n] != -1)
		return dp[n];
	dp[n] = tiling(n - 1) +tiling(n - 2);
	dp[n] %= mod;
	return dp[n];
}

int main() {
	int n;
	for (int i = 0; i < 1001; i++)
		dp[i] = -1;
	cin >> n;
	cout << tiling(n) << "\n";
	return 0;
}