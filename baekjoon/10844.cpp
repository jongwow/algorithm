#include <iostream>
#define mod 1000000000
#define INF 987654321
using namespace std;
int stairN[101][10]; //[a][b] : [현재 자리가 몇번째인지][현재 자리 정수 값]
/*
stairN[0][0] : 불가능 (0번째자리 없음)
stairN[0][1] : 불가능 (0번째자리 는 없음
stairN[1][0] : 불가능 (1번째자리는 가능하지만 0이 올 수는 없다.
stairN[1][1] : 가능 ( 1번째 자리에 1이 왔을 때 가능한 계단 수) = stairN[2][0] + stairN[2][2]
stairN[a][b] : (a번째 자리에 b가 왔을 때 계단 수) = stairN[a+1][b-1] + stairN[a+1][b+1]
	이때 a == N (끝에 도달)했을 경우는 return 1, b의 범위는 0<=b<=9
*/

int N; // 자리 수
int climb(int a, int b) {
	if (b < 0 || b > 9)//base case: beyond the scope.
		return 0;
	if (a == N) //base case : reached the end point
		return 1;
	if (stairN[a][b] != -1) //dp.
		return stairN[a][b];
	stairN[a][b] = climb(a + 1, b - 1) % mod + climb(a + 1, b + 1) % mod;
	stairN[a][b] %= mod;
	return stairN[a][b];
}

int climb2(int a, int b) {
	if (b < 0 || b > 9)
		return 0;
	if (a == 1)
		return 1;
	if (stairN[a][b] != -1)
		return stairN[a][b];
	stairN[a][b] = climb2(a - 1, b - 1) % mod + climb2(a - 1, b + 1) % mod;
	stairN[a][b] %= mod;
	return stairN[a][b];
}

int main() {
	cin >> N;
	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 101; j++)
			stairN[j][i] = -1;
	int res = 0;
	for (int i = 1; i < 10; i++){
		res += climb2(N, i);
		res %= mod;
	}
	cout << res << endl;
}