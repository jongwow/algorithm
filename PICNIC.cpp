#include <iostream>
#include <stdlib.h>
using namespace std;
bool friends[10][10];
int n, m;
int countPairing(bool taken[10]) {
	//taken[i] = i 번째 학생이 짝을 이미 찾았으면 true, 아니면 false.
	//base case: 모든 학생이 짝을 찾았으면 한 가지 방법을 찾았으니 종료한다.
	bool finished = true;
	for (int i = 0; i < n; i++) if (!taken[i]) finished = false;
	if (finished) return 1;
	int ret = 0;
	//서로 친구인 두 학생을 찾아 짝을 지어 준다.
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!taken[i] && !taken[j] && friends[i][j]) {
				taken[i] = taken[j] = true;
				ret += countPairing(taken);
				taken[i] = taken[j] = false;
			}
		}
	}
	return ret;
}

int countPairing2(bool taken[10]) {
	int firstFree = -1;
	for(int i=0; i<n; i++)
		if (!taken[i]) {
			firstFree = i;
			break;
		}
	//base case
	if (firstFree == -1) return 1;
	int ret = 0;
	for (int pairWith = firstFree + 1; pairWith < n; pairWith++) {
		if (!taken[pairWith] && friends[firstFree][pairWith]) {
			taken[firstFree] = taken[pairWith] = true;
			ret += countPairing2(taken);
			taken[firstFree] = taken[pairWith] = false;
		}
	}
	return ret;
}

/*
수도코드로 만들기
countPairing( taken ) : 짝이 있는지 확인하는 배열을 인자로 받아서 넘겨줌. 짝을 지은 쌍의 수를 반환.
기저사례: 모든 학생이 짝이 다 있을 때 짝지음 성공 -> return 1
짝이 없는 학생이 있을 때
	그 짝없는 학생과 친구인 학생을 찾는다. && 그 학생친구는 짝이 없어야 한다
		그 짝없는 학생과 친구학생을 짝을 맺어준다.
		그랬을 경우의 짝지음 숫자를 더해준다.
		그 짝없는 학생과 친구학생을 짝을 찢는다.
		//위의 부분은 백트레킹 부분. 공부했는데도 헷갈리는 구만.
	짝지음 숫자를 반환한다.
*/
int main() {
	freopen("input.txt", "r", stdin);
	int tc;
	cin >> tc;
	while (tc-- > 0) {
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < 10; j++)
				friends[i][j] = false;
		cin >> n >> m;
		int a, b;
		for (int i = 0; i < m; i++) {
			cin >> a >> b;
			friends[a][b] = friends[b][a] = true;
		}
		bool counts[10];
		for (int i = 0; i < n; i++) counts[i] = false;
		cout << countPairing2(counts) << endl;
	}
	
	return 0;
}