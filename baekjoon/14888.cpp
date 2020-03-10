#include <iostream>
#define INF 987654321
using namespace std;
int operators[4]; //연산자. 순서대로 + - * /
int A[11];//숫자.
int N; //수의 개수
int arithmeticOperation(int kIdx,bool isMin) {
	int result[4][2] = { 0,0,0,0,0,0,0,0 };
	if (kIdx == N - 1) return A[kIdx];
	for (int i = 0; i < 4; i++) {
		if (operators[i] > 0) {
			switch (i) {
			case 0:
				operators[i]--;
				result[i][0] = 1;
				result[i][1] = arithmeticOperation(kIdx + 1, isMin) + A[kIdx];
				operators[i]++;
				break;
			case 1:
				operators[i]--;
				result[i][0] = 1;
				result[i][1] = arithmeticOperation(kIdx + 1, isMin) - A[kIdx];
				operators[i]++;
				break;
			case 2:
				operators[i]--;
				result[i][0] = 1;
				result[i][1] = arithmeticOperation(kIdx + 1, isMin) * A[kIdx];
				operators[i]++;
				break;
			case 3:
				operators[i]--;
				result[i][0] = 1;
				result[i][1] = arithmeticOperation(kIdx + 1, isMin) / A[kIdx];
				operators[i]++;
				break;
			}
		}
	}
	int criteria = (isMin) ? INF : -INF;
	for (int i = 0; i < 4; i++) {
		if (result[i][0]) {
			if (isMin && result[i][1] < criteria)
				criteria = result[i][1];
			if (!isMin && result[i][1] > criteria)
				criteria = result[i][1];
		}
	}
	return criteria;
}
int main() {
	cin >> N;
	for (int i = 0; i < N; i++) 
		cin >> A[N-i-1];
	for (int i = 0; i < 4; i++) 
		cin >> operators[i];
	cout << arithmeticOperation(0, false) << endl;
	cout << arithmeticOperation(0, true) << endl;
	return 0;
}