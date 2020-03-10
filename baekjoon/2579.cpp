#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;
int dp[301][2];
int Stairs[301];
int stairsHeight;
int stepping(int st, int status) { //status == 0 이전에 안밟음 ==1 밟음
	if (st == stairsHeight-1) //마지막 계단에 도달하면
		return Stairs[st];
	if (st > stairsHeight-1) //마지막을 넘어가면 
		return -INF; //아주 큰 음의 정수를 반환해서 정답이 안되게 함.
	if (dp[st][status]!=0) //이미 계산한 부분문제일 경우
		return dp[st][status]; //dp를 반환.
	if (status == 0) //이전에 밟지 않았으면 2계단 or 1계단 둘다 가능
		dp[st][status] = max(stepping(st + 1, 1), stepping(st + 2, 0)) + Stairs[st];
	else //이전에 밟았으면 2계단만 가능
		dp[st][status] = stepping(st + 2, 0)+Stairs[st];
	return dp[st][status];
}

int main() {
	cin >> stairsHeight;
	for (int i = 0; i < stairsHeight; i++)
		cin >> Stairs[i];
	//처음에 1계단하느냐 2계단하느냐는 stepping에서 구분 못하므로
	//직접 max로 해줌.
	cout << max(stepping(0, 0),stepping(1,0)) << endl;
	return 0;
}