#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N;
	int A[101];
	int B[101];
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	for (int i = 0; i < N; i++) {
		cin >> B[i];
	}
	sort(A, A + N);
	sort(B, B + N);
	int res = 0;
	for (int i = 0; i < N; i++) {
		res += A[N-1-i] * B[i];
	}
	cout << res << endl;
	return 0;
}