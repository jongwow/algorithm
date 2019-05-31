#include <iostream>
#include <vector>
using namespace std;
bool friends[901][901];
int res[63];
int K, N, F;
void pushPairs(int picnic[63], int depth) {
	int first = 0;
	for (int i = 1; i <= K; i++) {
		if (!picnic[i]) {
			first = i;
			break;
		}
	}
	if (first == 0 || depth == N) {
		//cout << "EXIT" << endl;
		for (int i = 1; i <= K; i++) {
			res[i] = picnic[i];
		}
		for (int i = 1; i <= K; i++) {
			cout << i << ": " << res[i] << "\n";
		}
		cout << "====\n";
		return;
	}
	for (int next = first + 1; next <= N; next++) {
		//cout << "TEST" << endl;
		bool flag = true;
		for (int prev = 1; prev <= first; prev++) {
			if (!friends[prev][next]) flag = false;
		}
		if (flag) {
			//cout << "HEY" << endl;
			picnic[first + 1] = next;
			pushPairs(picnic, depth + 1);
			picnic[first + 1] = 0;
		}
	}
	//cout << "push(" << depth << ")\n";
	return;
}
/*
int* makePairing(int picnic[63], int depth) {
	int first = -1;
	for (int i = 0; i < K; i++) {
		if (!picnic[i]) {
			first = i;
			break;
		}
	}
	if (first == -1) return picnic;
	if (depth == N) {
		cout << "depth" << endl;
		return picnic;
	}
	vector<int> 
	for (int next = first + 1; next < N; next++) {
		bool flag = true;
		for (int cur = 0; cur <= first; cur++) {
			if (!friends[cur][next]) flag = false;
		}
		if (flag) {
			picnic[first + 1] = next;   
			picnic[first + 1] = 0;
		}
		else {
			continue;
		}
	}
	return ret;
}
*/
int main() {
	freopen("input.txt", "r", stdin);
	cin >> K >> N >> F;
	int a, b;
	for (int i = 0; i < 901; i++)
		for (int j = 0; j < 901; j++)
			friends[i][j] = false;
	for (int i = 0; i < F; i++) {
		cin >> a >> b;
		friends[a][b] = friends[b][a] = true;
	}
	int picnic[63];
	for (int i = 0; i < 63; i++)
		picnic[i] = 0;
	pushPairs(picnic, 0);
	for (int i = 1; i <= K; i++) {
		cout << i << ": " << res[i] << "\n";
	}
	cout << "====\n";
	return 0;
}