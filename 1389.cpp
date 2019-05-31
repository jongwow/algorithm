#include <iostream>
#include <vector>
#define INF 12345678
using namespace std;
int friends[100][100];
int n, m;
void init() {
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			friends[i][j] = m;
	}
}
int main() {
	int mini = INF;
	cin >> n >> m;
	int a, b;
	init();
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		friends[a-1][b-1] = 1;
		friends[b-1][a-1] = 1;
	}
	for (int k = 0; k < n; k++) {
		for (int s = 0; s < n; s++) {
			for (int e = 0; e < n; e++) {
				if (friends[s][e] > friends[s][k] + friends[k][e]) {
					friends[s][e] = friends[s][k] + friends[k][e];
				}
					
			}
		}
	}
	int idx = 0;
	for (int i = 0; i < n; i++){
		int sum = 0;
		for (int j = 0; j < n; j++) {
			sum += friends[i][j];
		}
		if (sum < mini){
			mini = sum;
			idx = i;
		}
	}
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++)
			cout << friends[i][j];
	cout << endl;
	}
	cout << idx+1 << endl;
	return 0;
}